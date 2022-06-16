import pandas as pd
import numpy as np
from matplotlib import pyplot
import dlib
import cv2
from imutils import face_utils
from pyparsing import col

#----------------------
#フレーム毎に処理を行う関数
#----------------------
def frame_process(img, frame_count):
    
    #グレースケールに変換
    img_gry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #顔を検出する
    faces = face_detector(img_gry, 1)

    if len(faces) == 0: #顔検出ができていなかったら
        return

    else: #顔検出出来ていたら
        #書き換えポイント
        file_name = "/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_csv/iwata/hsv_data/hsv_data" + str(frame_count) + ".csv"
        f = open(file_name, "a") #追記モードでファイルを開く
        f.write("R Value" + "," + "G Value" + "," + "B Value" + "," + "R+G+B Value" + "," + "R-B Value" + "\n") #ヘッダー作成
        
        #検出した全顔に対して処理を行う
        for face in faces:
            #顔のランドマーク検出
            landmark = face_predictor(img_gry, face)
            #処理の高速化のためランドマーク群をnumpy配列に変換する
            landmark = face_utils.shape_to_np(landmark)

        #--------------------------
        #鼻部のデータ取得・成形
        #--------------------------

        #ランドマークの番号を用いて画像の切り取りを行う
        #鼻の範囲としてx座標=32~36, y座標=28~34
        landmark_n32_x = landmark[31][0]
        landmark_n36_x = landmark[35][0]
        landmark_n28_y = landmark[27][1]
        landmark_n34_y = landmark[33][1]

        #画像の切り出し
        img2 = img[landmark_n28_y:landmark_n34_y, landmark_n32_x:landmark_n36_x]
        #鼻部の画像サイズ等の取り出し
        height_img2, weight_img2, channal_img2 = img2.shape

        #配列にする
        img_array = np.asarray(img2)

        #取り出した鼻部を1ピクセルずつ見ていく
        for i in range(0, height_img2):
            for j in range(0, weight_img2):
                R_value = int(img_array[i, j, :][2]) #V値の取得
                G_value = int(img_array[i, j, :][1]) #S値の取得
                B_value = int(img_array[i, j, :][0]) #H値の取得
                RGB_Value = R_value + G_value + B_value
                RB_Value = R_value - B_value

                f.write(str(R_value) + "," + str(G_value) + "," + str(B_value) + "," + str(RGB_Value) + "," + str(RB_Value) + "\n")

    f.close()
    make_cut_data(frame_count)
    return


def make_cut_data(frame_count):

    #先の関数で作った1フレームの各成分値のデータ
    file_name = "/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_csv/iwata/hsv_data/hsv_data" + str(frame_count) + ".csv"

    # データの読み込み
    df = pd.read_csv(file_name, encoding="utf-8")

    count07 = pd.DataFrame(columns=["R Value", "G Value", "B Value", "R+G+B Value", "R-B Value"])
    count815 = pd.DataFrame(columns=["R Value", "G Value", "B Value", "R+G+B Value", "R-B Value"])
    count1623 = pd.DataFrame(columns=["R Value", "G Value", "B Value", "R+G+B Value", "R-B Value"])
    count2431 = pd.DataFrame(columns=["R Value", "G Value", "B Value", "R+G+B Value", "R-B Value"])
    count3239 = pd.DataFrame(columns=["R Value", "G Value", "B Value", "R+G+B Value", "R-B Value"])
    count4047 = pd.DataFrame(columns=["R Value", "G Value", "B Value", "R+G+B Value", "R-B Value"])
    count4855 = pd.DataFrame(columns=["R Value", "G Value", "B Value", "R+G+B Value", "R-B Value"])
    count5663 = pd.DataFrame(columns=["R Value", "G Value", "B Value", "R+G+B Value", "R-B Value"])
    count6471 = pd.DataFrame(columns=["R Value", "G Value", "B Value", "R+G+B Value", "R-B Value"])
    count7279 = pd.DataFrame(columns=["R Value", "G Value", "B Value", "R+G+B Value", "R-B Value"])
    count8087 = pd.DataFrame(columns=["R Value", "G Value", "B Value", "R+G+B Value", "R-B Value"])
    count8895 = pd.DataFrame(columns=["R Value", "G Value", "B Value", "R+G+B Value", "R-B Value"])
    count96103 = pd.DataFrame(columns=["R Value", "G Value", "B Value", "R+G+B Value", "R-B Value"])
    count104111 = pd.DataFrame(columns=["R Value", "G Value", "B Value", "R+G+B Value", "R-B Value"])
    count112119 = pd.DataFrame(columns=["R Value", "G Value", "B Value", "R+G+B Value", "R-B Value"])
    count120127 = pd.DataFrame(columns=["R Value", "G Value", "B Value", "R+G+B Value", "R-B Value"])
    count128135 = pd.DataFrame(columns=["R Value", "G Value", "B Value", "R+G+B Value", "R-B Value"])
    count136143 = pd.DataFrame(columns=["R Value", "G Value", "B Value", "R+G+B Value", "R-B Value"])
    count144151 = pd.DataFrame(columns=["R Value", "G Value", "B Value", "R+G+B Value", "R-B Value"])
    count152159 = pd.DataFrame(columns=["R Value", "G Value", "B Value", "R+G+B Value", "R-B Value"])
    count160167 = pd.DataFrame(columns=["R Value", "G Value", "B Value", "R+G+B Value", "R-B Value"])
    count168175 = pd.DataFrame(columns=["R Value", "G Value", "B Value", "R+G+B Value", "R-B Value"])
    count176183 = pd.DataFrame(columns=["R Value", "G Value", "B Value", "R+G+B Value", "R-B Value"])
    count184191 = pd.DataFrame(columns=["R Value", "G Value", "B Value", "R+G+B Value", "R-B Value"])
    count192199 = pd.DataFrame(columns=["R Value", "G Value", "B Value", "R+G+B Value", "R-B Value"])
    count200207 = pd.DataFrame(columns=["R Value", "G Value", "B Value", "R+G+B Value", "R-B Value"])
    count208215 = pd.DataFrame(columns=["R Value", "G Value", "B Value", "R+G+B Value", "R-B Value"])
    count216223 = pd.DataFrame(columns=["R Value", "G Value", "B Value", "R+G+B Value", "R-B Value"])
    count224231 = pd.DataFrame(columns=["R Value", "G Value", "B Value", "R+G+B Value", "R-B Value"])
    count232239 = pd.DataFrame(columns=["R Value", "G Value", "B Value", "R+G+B Value", "R-B Value"])
    count240247 = pd.DataFrame(columns=["R Value", "G Value", "B Value", "R+G+B Value", "R-B Value"])
    count248255 = pd.DataFrame(columns=["R Value", "G Value", "B Value", "R+G+B Value", "R-B Value"])

    count = len(df_left["H Value"])
    for i in range(count):
        if float(df_left.at[df_left.index[i], "H Value"]) < 8:
            count07+= 1
        elif float(df_left.at[df_left.index[i], "H Value"]) < 16 and float(df_left.at[df_left.index[i], "H Value"]) >= 8:
            count815+= 1
        elif float(df_left.at[df_left.index[i], "H Value"]) < 24 and float(df_left.at[df_left.index[i], "H Value"]) >= 16:
            count1623+= 1
        elif float(df_left.at[df_left.index[i], "H Value"]) < 32 and float(df_left.at[df_left.index[i], "H Value"]) >= 24:
            count2431+= 1
        elif float(df_left.at[df_left.index[i], "H Value"]) < 40 and float(df_left.at[df_left.index[i], "H Value"]) >= 32:
            count3239+= 1
        elif float(df_left.at[df_left.index[i], "H Value"]) < 48 and float(df_left.at[df_left.index[i], "H Value"]) >= 40:
            count4047+= 1
        elif float(df_left.at[df_left.index[i], "H Value"]) < 56 and float(df_left.at[df_left.index[i], "H Value"]) >= 48:
            count4855+= 1
        elif float(df_left.at[df_left.index[i], "H Value"]) < 64 and float(df_left.at[df_left.index[i], "H Value"]) >= 56:
            count5663+= 1
        elif float(df_left.at[df_left.index[i], "H Value"]) < 72 and float(df_left.at[df_left.index[i], "H Value"]) >= 64:
            count6471+= 1
        elif float(df_left.at[df_left.index[i], "H Value"]) < 80 and float(df_left.at[df_left.index[i], "H Value"]) >= 72:
            count7279+= 1
        elif float(df_left.at[df_left.index[i], "H Value"]) < 88 and float(df_left.at[df_left.index[i], "H Value"]) >= 80:
            count8087+= 1
        elif float(df_left.at[df_left.index[i], "H Value"]) < 96 and float(df_left.at[df_left.index[i], "H Value"]) >= 88:
            count8895+= 1
        elif float(df_left.at[df_left.index[i], "H Value"]) < 104 and float(df_left.at[df_left.index[i], "H Value"]) >= 96:
            count96103+= 1
        elif float(df_left.at[df_left.index[i], "H Value"]) < 112 and float(df_left.at[df_left.index[i], "H Value"]) >= 104:
            count104111+= 1
        elif float(df_left.at[df_left.index[i], "H Value"]) < 120 and float(df_left.at[df_left.index[i], "H Value"]) >= 112:
            count112119+= 1
        elif float(df_left.at[df_left.index[i], "H Value"]) < 128 and float(df_left.at[df_left.index[i], "H Value"]) >= 120:
            count120127+= 1
        elif float(df_left.at[df_left.index[i], "H Value"]) < 136 and float(df_left.at[df_left.index[i], "H Value"]) >= 128:
            count128135+= 1
        elif float(df_left.at[df_left.index[i], "H Value"]) < 144 and float(df_left.at[df_left.index[i], "H Value"]) >= 136:
            count136143+= 1
        elif float(df_left.at[df_left.index[i], "H Value"]) < 152 and float(df_left.at[df_left.index[i], "H Value"]) >= 144:
            count144151+= 1
        elif float(df_left.at[df_left.index[i], "H Value"]) < 160 and float(df_left.at[df_left.index[i], "H Value"]) >= 152:
            count152159+= 1
        elif float(df_left.at[df_left.index[i], "H Value"]) < 168 and float(df_left.at[df_left.index[i], "H Value"]) >= 160:
            count160167+= 1
        elif float(df_left.at[df_left.index[i], "H Value"]) < 176 and float(df_left.at[df_left.index[i], "H Value"]) >= 168:
            count168175+= 1
        elif float(df_left.at[df_left.index[i], "H Value"]) < 184 and float(df_left.at[df_left.index[i], "H Value"]) >= 176:
            count176183+= 1
        elif float(df_left.at[df_left.index[i], "H Value"]) < 192 and float(df_left.at[df_left.index[i], "H Value"]) >= 184:
            count184191+= 1
        elif float(df_left.at[df_left.index[i], "H Value"]) < 200 and float(df_left.at[df_left.index[i], "H Value"]) >= 192:
            count192199+= 1
        elif float(df_left.at[df_left.index[i], "H Value"]) < 208 and float(df_left.at[df_left.index[i], "H Value"]) >= 200:
            count200207+= 1
        elif float(df_left.at[df_left.index[i], "H Value"]) < 216 and float(df_left.at[df_left.index[i], "H Value"]) >= 208:
            count208215+= 1
        elif float(df_left.at[df_left.index[i], "H Value"]) < 224 and float(df_left.at[df_left.index[i], "H Value"]) >= 216:
            count216223+= 1
        elif float(df_left.at[df_left.index[i], "H Value"]) < 232 and float(df_left.at[df_left.index[i], "H Value"]) >= 224:
            count224231+= 1
        elif float(df_left.at[df_left.index[i], "H Value"]) < 240 and float(df_left.at[df_left.index[i], "H Value"]) >= 232:
            count232239+= 1
        elif float(df_left.at[df_left.index[i], "H Value"]) < 248 and float(df_left.at[df_left.index[i], "H Value"]) >= 240:
            count240247+= 1
        elif float(df_left.at[df_left.index[i], "H Value"]) < 256 and float(df_left.at[df_left.index[i], "H Value"]) >= 248:
            count248255+= 1



#-------------------
#グラフを描く関数
#-------------------
def make_graph(frame_count):

    file_name = "/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_csv/iwata/hsv_data/hsv_data" + str(frame_count) + ".csv"

    # データの読み込み
    df = pd.read_csv(file_name, encoding="utf-8")

    # 使いたいデータをndarray型に変換する
    data_h = np.array(df["H Value"])
    # ヒストグラムを作成
    fig_h = pyplot.figure()
    ax_h = fig_h.add_subplot(1, 1, 1)
    ax_h.hist(data_h, bins=32, ec="black", range=(0, 255), color="red")
    file_name_h = "/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_graph/iwata/frame_data/h" + str(frame_count) + ".png"
    #グラフの諸設定(data_h)
    pyplot.title("H Value Frequency") #グラフタイトル
    pyplot.xlabel("Value") #x軸
    pyplot.yticks(np.arange(0, 5000, 600))

    # 使いたいデータをndarray型に変換する
    data_s = np.array(df["S Value"])
    # ヒストグラムを作成
    fig_s = pyplot.figure()
    ax_s = fig_s.add_subplot(1, 1, 1)
    ax_s.hist(data_s, bins=16, ec="black", range=(0, 255), color="green")
    file_name_s = "/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_graph/iwata/frame_data/s" + str(frame_count) + ".png"
    #グラフの諸設定(data_s)
    pyplot.title("S Value Frequency") #グラフタイトル
    pyplot.xlabel("Value") #x軸
    pyplot.yticks(np.arange(0, 3200, 600))

    # 使いたいデータをndarray型に変換する
    data_v = np.array(df["V Value"])
    # ヒストグラムを作成
    fig_v = pyplot.figure()
    ax_v = fig_v.add_subplot(1, 1, 1)
    ax_v.hist(data_v, bins=16, ec="black", range=(0, 255), color="blue")
    file_name_v = "/Users/shimizu_italab/Desktop/Study/HSV_Experiment/result_graph/iwata/frame_data/v" + str(frame_count) + ".png"
    #グラフの諸設定(data_v)
    pyplot.title("V Value Frequency") #グラフタイトル
    pyplot.xlabel("Value") #x軸
    pyplot.yticks(np.arange(0, 2600, 600))

    pyplot.close(fig_h)
    pyplot.close(fig_s)
    pyplot.close(fig_v)

    # グラフの出力
    fig_h.savefig(file_name_h)
    fig_s.savefig(file_name_s)
    fig_v.savefig(file_name_v)


#-------------
#メイン関数
#-------------
if __name__=="__main__":

    count = 1 #全フレーム(1秒に30枚)に対してランドマークはしないのでカウントフラグを使う
    frame_count = 1 #CSVファイルの時間を書き込むためのカウント

    #顔のランドマーク検出のための前準備
    face_detector = dlib.get_frontal_face_detector()
    predictor_path = "/Users/shimizu_italab/Desktop/Study/HSV_Experiment/analysis_code/shape_predictor_68_face_landmarks.dat"
    face_predictor = dlib.shape_predictor(predictor_path)

    #ビデオを読み込みする
    #書き換えポイント1
    cap = cv2.VideoCapture("/Users/shimizu_italab/Desktop/Study/HSV_Experiment/Experiment_movie/trim_movie(iwata).avi")

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


    cap.release()