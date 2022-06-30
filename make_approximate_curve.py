import pandas as pd
import numpy as np
from matplotlib import pyplot
import dlib
import cv2
from imutils import face_utils
from pyparsing import col
import numpy.polynomial.polynomial as P

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
        file_name = "\\\\LAB413//share413\\個人用フォルダ\\M1 Shimizu\\Experiment&analysis_code\\my_result\\yoshino_analysis\\cut_csv\\frame" + str(frame_count) + "\\" + str(count) + str(count+7) + ".csv"
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
    file_name = "\\\\LAB413//share413\\個人用フォルダ\\M1 Shimizu\\Experiment&analysis_code\\my_result\\yoshino_analysis\\cut_csv\\frame" + str(frame_count) + "\\" + str(count) + str(count+7) + ".csv"

    # データの読み込み
    df = pd.read_csv(file_name, encoding="utf-8")

    count = 0

    for i in range(32):
        new_df =  pd.DataFrame(columns=["R Value", "G Value", "B Value", "R+G+B Value", "R-B Value"])
        new_df_name = "\\\\LAB413//share413\\個人用フォルダ\\M1 Shimizu\\Experiment&analysis_code\\my_result\\yoshino_analysis\\cut_csv\\frame" + str(frame_count) + "\\" + str(count) + str(count+7) + ".csv"
        new_df.to_csv(new_df_name)
        count = count + 8


    total_data_number = len(df["R+G+B Value"]) #1フレーム内の全ピクセル数を求める

    for i in range(total_data_number):
        if float(df.at[df.index[i], "R+G+B Value"]) < 8:
            f = open("\\\\LAB413//share413\\個人用フォルダ\\M1 Shimizu\\Experiment&analysis_code\\my_result\\yoshino_analysis\\cut_csv\\frame" + str(frame_count) + "\\07.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 16 and float(df.at[df.index[i], "R+G+B Value"]) >= 8:
            f = open("\\\\LAB413//share413\\個人用フォルダ\\M1 Shimizu\\Experiment&analysis_code\\my_result\\yoshino_analysis\\cut_csv\\frame" + str(frame_count) + "\\815.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 24 and float(df.at[df.index[i], "R+G+B Value"]) >= 16:
            f = open("\\\\LAB413//share413\\個人用フォルダ\\M1 Shimizu\\Experiment&analysis_code\\my_result\\yoshino_analysis\\cut_csv\\frame" + str(frame_count) + "\\1623.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 32 and float(df.at[df.index[i], "R+G+B Value"]) >= 24:
            f = open("\\\\LAB413//share413\\個人用フォルダ\\M1 Shimizu\\Experiment&analysis_code\\my_result\\yoshino_analysis\\cut_csv\\frame" + str(frame_count) + "\\2431.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 40 and float(df.at[df.index[i], "R+G+B Value"]) >= 32:
            f = open("\\\\LAB413//share413\\個人用フォルダ\\M1 Shimizu\\Experiment&analysis_code\\my_result\\yoshino_analysis\\cut_csv\\frame" + str(frame_count) + "\\3239.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 48 and float(df.at[df.index[i], "R+G+B Value"]) >= 40:
            f = open("\\\\LAB413//share413\\個人用フォルダ\\M1 Shimizu\\Experiment&analysis_code\\my_result\\yoshino_analysis\\cut_csv\\frame" + str(frame_count) + "\\4047.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 56 and float(df.at[df.index[i], "R+G+B Value"]) >= 48:
            f = open("\\\\LAB413//share413\\個人用フォルダ\\M1 Shimizu\\Experiment&analysis_code\\my_result\\yoshino_analysis\\cut_csv\\frame" + str(frame_count) + "\\4855.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 64 and float(df.at[df.index[i], "R+G+B Value"]) >= 56:
            f = open("\\\\LAB413//share413\\個人用フォルダ\\M1 Shimizu\\Experiment&analysis_code\\my_result\\yoshino_analysis\\cut_csv\\frame" + str(frame_count) + "\\5663.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 72 and float(df.at[df.index[i], "R+G+B Value"]) >= 64:
            f = open("\\\\LAB413//share413\\個人用フォルダ\\M1 Shimizu\\Experiment&analysis_code\\my_result\\yoshino_analysis\\cut_csv\\frame" + str(frame_count) + "\\6471.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 80 and float(df.at[df.index[i], "R+G+B Value"]) >= 72:
            f = open("\\\\LAB413//share413\\個人用フォルダ\\M1 Shimizu\\Experiment&analysis_code\\my_result\\yoshino_analysis\\cut_csv\\frame" + str(frame_count) + "\\7279.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 88 and float(df.at[df.index[i], "R+G+B Value"]) >= 80:
            f = open("\\\\LAB413//share413\\個人用フォルダ\\M1 Shimizu\\Experiment&analysis_code\\my_result\\yoshino_analysis\\cut_csv\\frame" + str(frame_count) + "\\8087.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 96 and float(df.at[df.index[i], "R+G+B Value"]) >= 88:
            f = open("\\\\LAB413//share413\\個人用フォルダ\\M1 Shimizu\\Experiment&analysis_code\\my_result\\yoshino_analysis\\cut_csv\\frame" + str(frame_count) + "\\8895.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 104 and float(df.at[df.index[i], "R+G+B Value"]) >= 96:
            f = open("\\\\LAB413//share413\\個人用フォルダ\\M1 Shimizu\\Experiment&analysis_code\\my_result\\yoshino_analysis\\cut_csv\\frame" + str(frame_count) + "\\96103.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 112 and float(df.at[df.index[i], "R+G+B Value"]) >= 104:
            f = open("\\\\LAB413//share413\\個人用フォルダ\\M1 Shimizu\\Experiment&analysis_code\\my_result\\yoshino_analysis\\cut_csv\\frame" + str(frame_count) + "\\104111.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 120 and float(df.at[df.index[i], "R+G+B Value"]) >= 112:
            f = open("\\\\LAB413//share413\\個人用フォルダ\\M1 Shimizu\\Experiment&analysis_code\\my_result\\yoshino_analysis\\cut_csv\\frame" + str(frame_count) + "\\112119.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 128 and float(df.at[df.index[i], "R+G+B Value"]) >= 120:
            f = open("\\\\LAB413//share413\\個人用フォルダ\\M1 Shimizu\\Experiment&analysis_code\\my_result\\yoshino_analysis\\cut_csv\\frame" + str(frame_count) + "\\120127.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 136 and float(df.at[df.index[i], "R+G+B Value"]) >= 128:
            f = open("\\\\LAB413//share413\\個人用フォルダ\\M1 Shimizu\\Experiment&analysis_code\\my_result\\yoshino_analysis\\cut_csv\\frame" + str(frame_count) + "\\128135.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 144 and float(df.at[df.index[i], "R+G+B Value"]) >= 136:
            f = open("\\\\LAB413//share413\\個人用フォルダ\\M1 Shimizu\\Experiment&analysis_code\\my_result\\yoshino_analysis\\cut_csv\\frame" + str(frame_count) + "\\136143.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 152 and float(df.at[df.index[i], "R+G+B Value"]) >= 144:
            f = open("\\\\LAB413//share413\\個人用フォルダ\\M1 Shimizu\\Experiment&analysis_code\\my_result\\yoshino_analysis\\cut_csv\\frame" + str(frame_count) + "\\144151.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 160 and float(df.at[df.index[i], "R+G+B Value"]) >= 152:
            f = open("\\\\LAB413//share413\\個人用フォルダ\\M1 Shimizu\\Experiment&analysis_code\\my_result\\yoshino_analysis\\cut_csv\\frame" + str(frame_count) + "\\152159.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 168 and float(df.at[df.index[i], "R+G+B Value"]) >= 160:
            f = open("\\\\LAB413//share413\\個人用フォルダ\\M1 Shimizu\\Experiment&analysis_code\\my_result\\yoshino_analysis\\cut_csv\\frame" + str(frame_count) + "\\160167.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 176 and float(df.at[df.index[i], "R+G+B Value"]) >= 168:
            f = open("\\\\LAB413//share413\\個人用フォルダ\\M1 Shimizu\\Experiment&analysis_code\\my_result\\yoshino_analysis\\cut_csv\\frame" + str(frame_count) + "\\168175.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 184 and float(df.at[df.index[i], "R+G+B Value"]) >= 176:
            f = open("\\\\LAB413//share413\\個人用フォルダ\\M1 Shimizu\\Experiment&analysis_code\\my_result\\yoshino_analysis\\cut_csv\\frame" + str(frame_count) + "\\176183.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 192 and float(df.at[df.index[i], "R+G+B Value"]) >= 184:
            f = open("\\\\LAB413//share413\\個人用フォルダ\\M1 Shimizu\\Experiment&analysis_code\\my_result\\yoshino_analysis\\cut_csv\\frame" + str(frame_count) + "\\184191.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 200 and float(df.at[df.index[i], "R+G+B Value"]) >= 192:
            f = open("\\\\LAB413//share413\\個人用フォルダ\\M1 Shimizu\\Experiment&analysis_code\\my_result\\yoshino_analysis\\cut_csv\\frame" + str(frame_count) + "\\192199.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 208 and float(df.at[df.index[i], "R+G+B Value"]) >= 200:
            f = open("\\\\LAB413//share413\\個人用フォルダ\\M1 Shimizu\\Experiment&analysis_code\\my_result\\yoshino_analysis\\cut_csv\\frame" + str(frame_count) + "\\200207.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 216 and float(df.at[df.index[i], "R+G+B Value"]) >= 208:
            f = open("\\\\LAB413//share413\\個人用フォルダ\\M1 Shimizu\\Experiment&analysis_code\\my_result\\yoshino_analysis\\cut_csv\\frame" + str(frame_count) + "\\208215.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 224 and float(df.at[df.index[i], "R+G+B Value"]) >= 216:
            f = open("\\\\LAB413//share413\\個人用フォルダ\\M1 Shimizu\\Experiment&analysis_code\\my_result\\yoshino_analysis\\cut_csv\\frame" + str(frame_count) + "\\216223.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 232 and float(df.at[df.index[i], "R+G+B Value"]) >= 224:
            f = open("\\\\LAB413//share413\\個人用フォルダ\\M1 Shimizu\\Experiment&analysis_code\\my_result\\yoshino_analysis\\cut_csv\\frame" + str(frame_count) + "\\224231.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 240 and float(df.at[df.index[i], "R+G+B Value"]) >= 232:
            f = open("\\\\LAB413//share413\\個人用フォルダ\\M1 Shimizu\\Experiment&analysis_code\\my_result\\yoshino_analysis\\cut_csv\\frame" + str(frame_count) + "\\232239.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 248 and float(df.at[df.index[i], "R+G+B Value"]) >= 240:
            f = open("\\\\LAB413//share413\\個人用フォルダ\\M1 Shimizu\\Experiment&analysis_code\\my_result\\yoshino_analysis\\cut_csv\\frame" + str(frame_count) + "\\240247.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 256 and float(df.at[df.index[i], "R+G+B Value"]) >= 248:
            f = open("\\\\LAB413//share413\\個人用フォルダ\\M1 Shimizu\\Experiment&analysis_code\\my_result\\yoshino_analysis\\cut_csv\\frame" + str(frame_count) + "\\248255.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
    
    make_graph(frame_count, total_data_number)



#-------------------
#グラフを描く関数
#-------------------
def make_graph(frame_count, total_data_number):

    count = 0
    for i in range(32):
        look_df_name = "\\\\LAB413//share413\\個人用フォルダ\\M1 Shimizu\\Experiment&analysis_code\\my_result\\yoshino_analysis\\cut_csv\\frame" + str(frame_count) + "\\" + str(count) + str(count+7) + ".csv"
        look_df = pd.read_csv(look_df_name, encoding="utf-8")

        fig = pyplot.figure()
        ax = fig.add_subplot(1, 1, 1)
        fig_name = "\\\\LAB413//share413\\個人用フォルダ\\M1 Shimizu\\Experiment&analysis_code\\my_result\\yoshino_analysis\\figure\\frame" + str(frame_count) + "\\" + str(count) + str(count+7) + ".png"

        pyplot.xlim(0, 765) #R+G+Bの最大値まで
        pyplot.ylim(0, 255)
        title = "Scatter of R+G+B" + str(count) + "~" + str(count+7) + "(frame" + str(frame_count) + ")"
        pyplot.title(title)
        pyplot.xlabel("R+G+B Value")
        pyplot.ylabel("R-B Value")

        approximate = P.polyfit(look_df['R+G+B Value'], look_df['R-B Value'], 1)
        approximate_formula = "y = " + str(approximate[0]) + " + " + str(approximate[1]) + " * x" #近似直線の式
        approximate_x = np.arange(count, count+7, 0.1)
        approximate_y = P.polyval(approximate_x, approximate)

        density = len(look_df["R+G+B Value"]) / total_data_number

        pyplot.scatter(look_df["R+G+B Value"], look_df["R-B Value"]) #散布図を描く
        pyplot.plot(approximate_x, approximate_y) #近似直線を描く

        pyplot.legend([density, approximate_formula])

        fig.savefig(fig_name)


#-------------
#メイン関数
#-------------
if __name__=="__main__":

    count = 1 #全フレーム(1秒に30枚)に対してランドマークはしないのでカウントフラグを使う
    frame_count = 1 #CSVファイルの時間を書き込むためのカウント

    #顔のランドマーク検出のための前準備
    face_detector = dlib.get_frontal_face_detector()
    predictor_path = "\\\\LAB413\share413\\個人用フォルダ\\M1 Shimizu\\Experiment&analysis_code\\analysis_code\\landmark\\shape_predictor_68_face_landmarks.dat"
    face_predictor = dlib.shape_predictor(predictor_path)

    #ビデオを読み込みする
    #書き換えポイント1
    cap = cv2.VideoCapture("\\\\LAB413\\share413\\個人用フォルダ\\B4 Yoshino\\video\\hino\\hino_yoko.mp4")

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