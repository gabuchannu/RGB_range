from cmath import pi
import pandas as pd
import numpy as np
from matplotlib import pyplot
import cv2
import face_mesh_matsumoto
from sklearn import linear_model

#----------------------
#フレーム毎に処理を行う関数
#----------------------
def frame_process(img, frame_count):
    
    facemesh = face_mesh_matsumoto.Facemesh(0.7, 0.5) #facemeshを呼びだす
    results = facemesh.run(img) #入ってきたフレーム画像に対してfacemeshを行う


    if results == None: #顔検出ができていなかったら
        return

    else: #顔検出出来ていたら
        #書き換えポイント
        file_name = ".//csv_result//hino//frame" + str(frame_count) + ".csv"
        f = open(file_name, "a") #追記モードでファイルを開く
        f.write("R Value" + "," + "G Value" + "," + "B Value" + "," + "R+G+B Value" + "," + "R-B Value" + "\n") #ヘッダー作成
        
        nose_img = results["nose"] #画像の切り出し

        height_nose, weight_nose, channal_nose = nose_img.shape #鼻部の画像サイズ等の取り出し

        #配列にする
        img_array = np.asarray(nose_img)

        #取り出した鼻部を1ピクセルずつ見ていく
        for i in range(0, height_nose):
            for j in range(0, weight_nose):
                R_value = int(img_array[i, j, :][2]) #R値の取得
                G_value = int(img_array[i, j, :][1]) #G値の取得
                B_value = int(img_array[i, j, :][0]) #B値の取得
                RGB_Value = R_value + G_value + B_value #R+G+B成分値を作る
                RB_Value = R_value - B_value #R-B成分値を作る

                f.write(str(R_value) + "," + str(G_value) + "," + str(B_value) + "," + str(RGB_Value) + "," + str(RB_Value) + "\n")

    f.close()
    make_cut_data(frame_count) #現在見ているフレーム数を持って値を切り取りする関数に渡す


def make_cut_data(frame_count):

    #先の関数で作った1フレームの各成分値のデータ
    file_name = ".//csv_result//hino//frame" + str(frame_count) + ".csv"
    
    data = [] #全てのデータを入れる配列を作成
    for i in range(106): #CSVの数だけ配列を作る
        data.append([]) #2次元配列にする

    # データの読み込み
    #df = pd.read_csv(file_name, encoding="shift_jis")
    df = pd.read_csv(file_name, encoding="utf-8")

    total_data_number = len(df["R+G+B Value"]) #1フレーム内の全ピクセル数を求める

    for i in range(106):
        for j in range(total_data_number): #全データを順繰りに見ていく
            #i行目の3列目(R+G+B成分値)
            if i == 0:
                if (df.iat[j, 3] // (32 + i * 7)) == 0:
                    pickup_data = [] #見ているデータを入れる配列
                    for k in range(5):
                        pickup_data.append(df.iat[j, k])
                    data[i].append(pickup_data)
            else:
                if ((df.iat[j, 3] // (32 + i * 7)) == 0) & (df.iat[j, 3] >= i * 7):
                    pickup_data = [] #見ているデータを入れる配列
                    for k in range(5):
                        pickup_data.append(df.iat[j, k])
                    data[i].append(pickup_data)

    count = 0

    for i in range(106): #CSVに書き込みしていく
        new_df =  pd.DataFrame(data[i], columns=["R Value", "G Value", "B Value", "R+G+B Value", "R-B Value"]) #新しいファイルを作成する
        new_df_name = ".//csv_result//hino//frame" + str(frame_count) + "_" + str(count) + str(count+31) + ".csv" #新しいCSVを作成する
        new_df.to_csv(new_df_name) #CSVに切ったデータを書き込む
        count = count + 7



#-------------------
#グラフを描く関数
#-------------------
def make_graph(frame_count):

    count = 0
    color = ["red", "coral", "gold", "yellowgreen", "forestgreen", "deepskyblue", "mediumblue", "darkviolet", "hotpink", "sienna", "grey", "black"]

    for i in range(106):
        total_data_x = [] #全フレームのi番目の範囲のデータを入れる
        total_data_y = []
        total_data_number = 0

        #グラフ作成の書式
        fig = pyplot.figure()
        ax = fig.add_subplot(1, 1, 1)
        fig_name = ".//figure_result//hino//frame_total_" + str(count) + str(count+31) + ".png" #ファイルの名前
        pyplot.xlim(0, 765) #R+G+Bの最大値まで
        pyplot.ylim(0, 255) #R-Bの最大値まで
        title = "Scatter of R+G+B" + str(count) + "~" + str(count+31) + "(total_frame)"
        pyplot.title(title)
        pyplot.xlabel("R+G+B Value")
        pyplot.ylabel("R-B Value")

        for j in range(frame_count-1):
            look_df_name = ".//csv_result//hino//frame" + str(j+1) + "_" + str(count) + str(count+31) + ".csv" #開くファイルの名前を指定
            look_df = pd.read_csv(look_df_name, encoding="utf-8") #CSVをDFとして開く

            if len(look_df["R+G+B Value"]) != 0: #要素が存在するのであれば
                for k in range(len(look_df["R+G+B Value"])):
                    total_data_x.append(look_df.iat[k,3])
                    total_data_y.append(look_df.iat[k,4])
                total_data_number = total_data_number + len(look_df["R-B Value"])
                pyplot.scatter(look_df["R+G+B Value"], look_df["R-B Value"], color = color[j]) #散布図を描く

        if total_data_number != 0:
            x_col = ["R+G+B Value"]
            y_col = ["R-B Value"]

            x_data_df = pd.DataFrame(data=total_data_x, columns=x_col)
            y_data_df = pd.DataFrame(data=total_data_y, columns=y_col)
            
            clf = linear_model.LinearRegression()     

            #近似直線を作るための傾きと切片を出す
            clf.fit(x_data_df, y_data_df)
            a = clf.coef_
            b = clf.intercept_

            if len(x_data_df) >= 2:
                r2 = clf.score(x_data_df, y_data_df)
            else:
                r2 = "NAN"

            approximate_formula = "y = " + str(f'{b[0]:.3f}') + " + " + str(f'{a[0][0]:.3f}') + " * x" #近似直線の式

            xinterval = 0.1 #近似直線を表示するためのxダミーデータを作る
            x = np.arange(count-30, count+37, xinterval)
            y = a[0] * x + b

            density = len(look_df["R+G+B Value"]) / total_data_number * 100 #密度を%で表示する

            if r2 == "NAN":
                text = "r^2:" + str(r2)
            else:
                text = "r^2:" + str(format(r2, '.2f'))

            pyplot.plot(x, y, color="coral") #近似直線を描く
            pyplot.text(20, 230, text)

            pyplot.legend(["density:" + f'{density:.3f}' + "%", "regressionline:" + approximate_formula])

            pyplot.close(fig)
            fig.savefig(fig_name)
        
            count = count + 7       


#-------------
#メイン関数
#-------------
if __name__=="__main__":

    count = 1 #全フレーム(1秒に30枚)に対してランドマークはしないのでカウントフラグを使う
    frame_count = 1 #CSVファイルの時間を書き込むためのカウント

    #ビデオを読み込みする
    #書き換えポイント1
    cap = cv2.VideoCapture(".//data_movie//hino_yoko.mp4")

    while True: #動画が終わるまで続ける
        ret, img = cap.read()

        if ret == False: #もしretがFalseだったら
            break #動画の画像は1つ前でなくなっているのでループから抜ける

        if count == 30: #1秒経過していたら
            count = 1 #カウンターを初期化
            frame_process(img, frame_count) #取り出したimgに対してランドマーク
            frame_count = frame_count + 1 #1増やす

        else: #countが30未満だったら
            count = count + 1 #countを増やす

    max_frame_count = frame_count
    make_graph(frame_count)

    cap.release()