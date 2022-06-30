import pandas as pd
import numpy as np
from matplotlib import pyplot
import cv2
from pyparsing import col
import numpy.polynomial.polynomial as P
import face_mesh_matsumoto
import make_csv

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
        file_name = "\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + ".csv"
        f = open(file_name, "a") #追記モードでファイルを開く
        f.write("R Value" + "," + "G Value" + "," + "B Value" + "," + "R+G+B Value" + "," + "R-B Value" + "\n") #ヘッダー作成
        
        nose_img = results['nose'] #画像の切り出し

        height_nose, weight_nose, channal_nose = nose_img.shape #鼻部の画像サイズ等の取り出し

        #配列にする
        img_array = np.asarray(nose_img)

        #取り出した鼻部を1ピクセルずつ見ていく
        for i in range(0, height_nose):
            for j in range(0, weight_nose):
                R_value = int(img_array[i, j, :][2]) #R値の取得
                G_value = int(img_array[i, j, :][1]) #G値の取得
                B_value = int(img_array[i, j, :][0]) #B値の取得
                RGB_Value = R_value + G_value + B_value
                RB_Value = R_value - B_value

                f.write(str(R_value) + "," + str(G_value) + "," + str(B_value) + "," + str(RGB_Value) + "," + str(RB_Value) + "\n")

    f.close()
    make_cut_data(frame_count)
    return


def make_cut_data(frame_count):

    #先の関数で作った1フレームの各成分値のデータ
    file_name = "\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + ".csv"

    # データの読み込み
    #df = pd.read_csv(file_name, encoding="utf-8")
    df = pd.read_csv(file_name, encoding="shift_jis")

    count = 0

    for i in range(32):
        new_df =  pd.DataFrame(columns=["R Value", "G Value", "B Value", "R+G+B Value", "R-B Value"])
        new_df_name = "\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\" + str(count) + str(count+7) + ".csv"
        new_df.to_csv(new_df_name)
        count = count + 8


    total_data_number = len(df["R+G+B Value"]) #1フレーム内の全ピクセル数を求める

    
    
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