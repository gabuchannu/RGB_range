from cmath import pi
import pandas as pd
import numpy as np
from matplotlib import pyplot
import cv2
import face_mesh_matsumoto
from sklearn import linear_model
import os

#----------------------
#フレーム毎に処理を行う関数
#----------------------
def frame_process(img, frame_count, interval, step, video_name):
    
    facemesh = face_mesh_matsumoto.Facemesh(0.7, 0.5) #facemeshを呼びだす
    results = facemesh.run(img) #入ってきたフレーム画像に対してfacemeshを行う


    if results == None: #顔検出ができていなかったら
        print("Can't take face.")
        #cv2.imwrite(".//result//figure_result//hino_check_face//" + str(frame_count) + ".png", img)
        return

    else: #顔検出出来ていたら
        #書き換えポイント
        file_name = ".//result//csv_result//" + str(video_name) + "_" + str(interval) + "_" + str(step) + "//frame" + str(frame_count) + ".csv"
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

        make_cut_data(frame_count, interval, step, video_name) #現在見ているフレーム数を持って値を切り取りする関数に渡す


def make_cut_data(frame_count, interval, step, video_name):

    #先の関数で作った1フレームの各成分値のデータ
    file_name = ".//result//csv_result//" + str(video_name) + "_" + str(interval) + "_" + str(step) + "//frame" + str(frame_count) + ".csv"
    #if ((765 - interval) % step) == 0:
    file_number = ((765 - interval) // (step - 1)) + 2 #何個のデータができるか計算する
    #else:
    #    file_number = ((765 - interval) // (step - 1)) + 1
    
    data = [] #全てのデータを入れる配列を作成
    for i in range(file_number): #CSVの数だけ配列を作る
        data.append([]) #2次元配列にする

    # データの読み込み
    #df = pd.read_csv(file_name, encoding="shift_jis")
    df = pd.read_csv(file_name, encoding="utf-8")

    total_data_number = len(df["R+G+B Value"]) #1フレーム内の全ピクセル数を求める

    for i in range(file_number):
        for j in range(total_data_number): #全データを順繰りに見ていく
            if i == 0:
                if (df.iat[j, 3] // (interval + i * (step - 1))) == 0: #j行目の3列目(R+G+B成分値)
                    pickup_data = [] #見ているデータを入れる配列
                    for k in range(5):
                        pickup_data.append(df.iat[j, k]) #R,G,B,R+G+B,R-B全部のデータを入れる
                    data[i].append(pickup_data) #追加する
            else:
                if ((df.iat[j, 3] // (interval + i * (step - 1))) == 0) & (df.iat[j, 3] >= i * (step - 1)): #j行目の3列目(R+G+B成分値)
                    pickup_data = [] #見ているデータを入れる配列
                    for k in range(5):
                        pickup_data.append(df.iat[j, k]) #R,G,B,R+G+B,R-B全部のデータを入れる
                    data[i].append(pickup_data) #追加する

    count = 0

    for i in range(file_number): #CSVに書き込みしていく
        new_df =  pd.DataFrame(data[i], columns=["R Value", "G Value", "B Value", "R+G+B Value", "R-B Value"]) #新しいファイルを作成する
        new_df_name = ".//result//csv_result//" + str(video_name) + "_" + str(interval) + "_" + str(step) + "//frame" + str(frame_count) + "_" + str(count) + str(count + interval - 1) + ".csv" #新しいCSVを作成する
        new_df.to_csv(new_df_name) #CSVに切ったデータを書き込む
        count = count + step - 1
    
    make_graph(frame_count, total_data_number, interval, step, file_number, video_name)



#-------------------
#グラフを描く関数
#-------------------
def make_graph(frame_count, total_data_number, interval, step, file_number, video_name):

    count = 0
    for i in range(file_number):
        look_df_name = ".//result//csv_result//" + str(video_name) + "_" + str(interval) + "_" + str(step) + "//frame" + str(frame_count) + "_" + str(count) + str(count + interval - 1) + ".csv" #開くファイルの名前を指定
        #look_df = pd.read_csv(look_df_name, encoding="shift_jis")
        look_df = pd.read_csv(look_df_name, encoding="utf-8") #CSVをDFとして開く

        if len(look_df["R+G+B Value"]) != 0: #要素が存在するのであれば

            fig = pyplot.figure()
            ax = fig.add_subplot(1, 1, 1)
            fig_name = ".//result//figure_result//" + str(video_name) + "_" + str(interval) + "_" + str(step) + "//frame" + str(frame_count) + "_" + str(count) + str(count + interval - 1) + ".png" #ファイルの名前

            pyplot.xlim(0, 765) #R+G+Bの最大値まで
            pyplot.ylim(0, 255) #R-Bの最大値まで
            title = "Scatter of R+G+B" + str(count) + "~" + str(count + interval - 1) + "(frame" + str(frame_count) + ")"
            pyplot.title(title)
            pyplot.xlabel("R+G+B Value")
            pyplot.ylabel("R-B Value")

            clf = linear_model.LinearRegression()

            x_data = look_df[["R+G+B Value"]] #xのデータとしてR+G+B成分値
            y_data = look_df[["R-B Value"]] #yのデータとしてR-B成分値

            #近似直線を作るための傾きと切片を出す
            clf.fit(x_data, y_data)
            a = clf.coef_
            b = clf.intercept_

            if len(x_data) >= 2:
                r2 = clf.score(x_data, y_data)
            else:
                r2 = "NAN"

            approximate_formula = "y = " + str(f'{b[0]:.3f}') + " + " + str(f'{a[0][0]:.3f}') + " * x" #近似直線の式

            xinterval = 0.1 #近似直線を表示するためのxダミーデータを作る
            x = np.arange(count-80, count+80, xinterval)
            y = a[0][0] * x + b[0]

            density = len(look_df["R+G+B Value"]) / total_data_number * 100 #密度を%で表示する

            # if r2 == "NAN":
            #     text = "r^2:" + str(r2)
            # else:
            #     text = "r^2:" + str(format(r2, '.2f'))

            pyplot.scatter(look_df["R+G+B Value"], look_df["R-B Value"]) #散布図を描く
            pyplot.plot(x, y, color="coral") #近似直線を描く
            # pyplot.text(20, 230, text)

            pyplot.legend(["density:" + f'{density:.3f}' + "%", "regressionline:" + approximate_formula])

            fig.savefig(fig_name)
            pyplot.close(fig)
        
        count = count + step - 1


#-------------
#メイン関数
#-------------
if __name__=="__main__":

    interval = int(input("範囲の幅を数値入力してください："))
    step = int(input("ずらしていく幅を数値入力してください："))

    count = 1 #全フレーム(1秒に30枚)に対してランドマークはしないのでカウントフラグを使う

    video_count = 0 #全ての動画に対して処理を行うためのカウント

    while True:
        video_name_path = ".//all_movie_path.txt" #ビデオを読み込みする
        with open(video_name_path) as f:
            all_video = f.read().splitlines() #リストにする

            frame_count = 1 #CSVファイルの時間を書き込むためのカウント

            try: #例外処理
                cap = cv2.VideoCapture(".//data_movie//" + str(all_video[video_count])) #動画を読み込む
            except IndexError: #読み込む動画の配列がなくなったら
                break #抜ける

            video_name = all_video[video_count].split(".")[0] #.mp4以前の名前を取得する

            #CSVフォルダを作成する
            csv_path = ".//result//csv_result//" + str(video_name) + "_" + str(interval) + "_" + str(step)
            os.mkdir(csv_path)
            #グラフフォルダを作成する
            figure_path = ".//result//figure_result//" + str(video_name) + "_" + str(interval) + "_" + str(step)
            os.mkdir(figure_path)

            while True: #動画が終わるまで続ける
                ret, img = cap.read()

                if ret == False: #もしretがFalseだったら
                    break #動画の画像は1つ前でなくなっているのでループから抜ける

                if count == 30: #1秒経過していたら
                    count = 1 #カウンターを初期化
                    frame_process(img, frame_count, interval, step, video_name) #取り出したimgに対してランドマーク
                    frame_count = frame_count + 1 #1増やす

                else: #countが30未満だったら
                    count = count + 1 #countを増やす

            cap.release() #動画を終了する
            video_count += 1 #次の動画を見るためにカウンターを増やす