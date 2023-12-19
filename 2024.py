import pyxel
import random

masu = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]


# 詰み判定を行うクラス
class Tumi:
    # 詰んでいるか詰んでいないかの判定を行うメソッド
    def hanntei(self, masu):
        # 初期値として1を設定。詰みでない状態を表します。
        self.tumi = 1
        
        # 盤面を走査して、0が存在するかどうかを確認します。
        for x in range(4):
            for y in range(4):
                # 盤面の要素が0の場合、詰んでいない状態としてself.tumiを0に更新します。
                if masu[x][y] == 0:
                    self.tumi = 0
        # 詰み判定の結果を返します。1ならば詰んでいない、0ならば詰んでいる状態です。
        return self.tumi


class App:
    def __init__(self):
        # Initialize Pyxel here
        pyxel.init(200, 200)

        self.scene = 0
        self.score = 0
        self.count = 0
        self.tumi = Tumi()
        pyxel.run(self.update, self.draw)

    def update(self):
        # シーン0: タイトル画面
        if self.scene == 0:
            # マウスカーソルを表示
            pyxel.mouse(True)
            
            # スタートボタンがクリックされたかどうかの判定
            if (
                (50 <= pyxel.mouse_x <= 150)
                and (50 <= pyxel.mouse_y <= 150)
                and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT)
            ):
                # シーンをゲーム中に切り替え、マウスカーソルを非表示
                self.scene = 1
                pyxel.mouse(False)
        
        # シーン1: ゲーム中
        if self.scene == 1:
            # ゲームの初回実行時の処理
            if self.count == 0:
                # 盤面を初期化
                for x in range(4):
                    for y in range(4):
                        masu[x][y] = 0
                
                # スコアを初期化および初期タイルの生成
                self.score = 0
                self.score += 1
                masu[pyxel.rndi(0, 3)][pyxel.rndi(0, 3)] = int(
                    pyxel.rndi(11, 20) / 10
                ) * 2
                self.count += 1

            # ユーザーの入力を処理
            self.handle_input()

            # 盤面に2048以上の数字が存在する場合、クリアシーンに切り替え
            for x in range(4):
                for y in range(4):
                    if masu[x][y] >= 2048:
                        self.scene = 3

    def handle_input(self):
        if pyxel.btnp(pyxel.KEY_RIGHT):
            self.move_right()
        elif pyxel.btnp(pyxel.KEY_LEFT):
            self.move_left()
        elif pyxel.btnp(pyxel.KEY_UP):
            self.move_up()
        elif pyxel.btnp(pyxel.KEY_DOWN):
            self.move_down()

    def move_right(self):
        # スコアを更新
        self.score += 1
        
        # タイルを右にスライドさせる処理
        for x in range(4):
            y = 0
            for y in range(3):
                # もし右側が空白であり、現在のタイルが2以上の場合、スライドさせる
                while masu[x][2 - y] >= 2 and masu[x][3 - y] == 0:
                    masu[x][3 - y] = masu[x][2 - y]
                    masu[x][2 - y] = 0
                    y -= 1
                    # yが-1になったらループ終了
                    if y == -1:
                        break

        # 右にスライドした後、同じ数字のタイルを結合する処理
        for x in range(4):
            for y in range(3):
                # もし隣り合う2つのタイルが同じ数字なら結合
                if masu[x][3 - y] == masu[x][2 - y]:
                    masu[x][3 - y] = 2 * masu[x][3 - y]
                    masu[x][2 - y] = 0

        # 再度、結合後に空いたスペースを埋める処理
        for x in range(4):
            y = 0
            for y in range(3):
                # もし右側が空白であり、現在のタイルが2以上の場合、スライドさせる
                while masu[x][2 - y] >= 2 and masu[x][3 - y] == 0:
                    masu[x][3 - y] = masu[x][2 - y]
                    masu[x][2 - y] = 0
                    y -= 1
                    # yが-1になったらループ終了
                    if y == -1:
                        break

        # 詰み判定および新しいタイル生成
        # それぞれのムーブの最後に結合判定を置くことによって、動かした上でまだ0だったら詰みというフローでコードを簡略化できる。
        self.tumi.tumi = self.tumi.hanntei(masu)
        self.spawn_new_tile()


    def move_left(self):
        self.score += 1
        for x in range(4):
            y = 0
            for y in range(3):
                while masu[x][y + 1] >= 2 and masu[x][y] == 0:
                    masu[x][y] = masu[x][y + 1]
                    masu[x][y + 1] = 0
                    y -= 1
                    if y == -1:
                        break
        for x in range(4):
            for y in range(3):
                if masu[x][y] == masu[x][y + 1]:
                    masu[x][y] = 2 * masu[x][y + 1]
                    masu[x][y + 1] = 0

        for x in range(4):
            y = 0
            for y in range(3):
                while masu[x][y + 1] >= 2 and masu[x][y] == 0:
                    masu[x][y] = masu[x][y + 1]
                    masu[x][y + 1] = 0
                    y -= 1
                    if y == -1:
                        break
        self.tumi.tumi = self.tumi.hanntei(masu)
        self.spawn_new_tile()


    def move_up(self):
        self.score += 1
        for y in range(4):
            x = 0
            for x in range(3):
                while masu[x + 1][y] >= 2 and masu[x][y] == 0:
                    masu[x][y] = masu[x + 1][y]
                    masu[x + 1][y] = 0
                    x -= 1
                    if x == -1:
                        break
        for y in range(4):
            for x in range(3):
                if masu[x][y] == masu[x + 1][y]:
                    masu[x][y] = 2 * masu[x + 1][y]
                    masu[x + 1][y] = 0

        for y in range(4):
            x = 0
            for x in range(3):
                while masu[x + 1][y] >= 2 and masu[x][y] == 0:
                    masu[x][y] = masu[x + 1][y]
                    masu[x + 1][y] = 0
                    x -= 1
                    if x == -1:
                        break
        self.tumi.tumi = self.tumi.hanntei(masu)
        self.spawn_new_tile()

    def move_down(self):
        self.score += 1
        for y in range(4):
            x = 0
            for x in range(3):
                while masu[2 - x][y] >= 2 and masu[3 - x][y] == 0:
                    masu[3 - x][y] = masu[2 - x][y]
                    masu[2 - x][y] = 0
                    x -= 1
                    if x == -1:
                        break
        for y in range(4):
            for x in range(3):
                if masu[3 - x][y] == masu[2 - x][y]:
                    masu[3 - x][y] = 2 * masu[3 - x][y]
                    masu[2 - x][y] = 0

        for y in range(4):
            x = 0
            for x in range(3):
                while masu[2 - x][y] >= 2 and masu[3 - x][y] == 0:
                    masu[3 - x][y] = masu[2 - x][y]
                    masu[2 - x][y] = 0
                    x -= 1
                    if x == -1:
                        break
        self.tumi.tumi = self.tumi.hanntei(masu)
        self.spawn_new_tile()


    def update(self):
        # シーン0: タイトル画面
        if self.scene == 0:
            # マウスカーソルを表示
            pyxel.mouse(True)
            
            # スタートボタンがクリックされたかどうかの判定
            if (
                (50 <= pyxel.mouse_x <= 150)
                and (50 <= pyxel.mouse_y <= 150)
                and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT)
            ):
                # シーンをゲーム中に切り替え、マウスカーソルを非表示
                self.scene = 1
                pyxel.mouse(False)
        
        # シーン1: ゲーム中
        if self.scene == 1:
            # ゲームの初回実行時の処理
            if self.count == 0:
                # 盤面を初期化
                for x in range(4):
                    for y in range(4):
                        masu[x][y] = 0
                
                # スコアを初期化および初期タイルの生成
                self.score = 0
                self.score += 1
                masu[pyxel.rndi(0, 3)][pyxel.rndi(0, 3)] = int(
                    pyxel.rndi(11, 20) / 10
                ) * 2
                self.count += 1

            # ユーザーの入力を処理
            self.handle_input()

            # 盤面に2048以上の数字が存在する場合、クリアシーンに切り替え
            for x in range(4):
                for y in range(4):
                    if masu[x][y] >= 2048:
                        self.scene = 3

        # シーン2: ゲームオーバー
        if self.scene == 2:
            # マウスカーソルを表示
            if (
                (0 <= pyxel.mouse_x <= 200)
                and (0 <= pyxel.mouse_y <= 200)
                and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT)
            ):
                # シーンをタイトルに戻し、カウントをリセット、マウスカーソルを非表示
                self.scene = 0
                self.count = 0
                pyxel.mouse(False)


    def draw(self):
        #シーンごとに、切り替えるだけ〜！
        if self.scene == 0:
            pyxel.cls(7)
            pyxel.rect(50, 50, 100, 100, 8)
            pyxel.text(90, 97, "start", 0)
        if self.scene == 1:
            pyxel.rect(20, 20, 160, 160, 14)
            for a in range(4):
                for b in range(4):
                    pyxel.rect(32 + 37 * a, 32 + 37 * b, 25, 25, 7)
            pyxel.text(5, 5, "2024", 3)

            for x in range(4):
                for y in range(4):
                    if masu[y][x] == 0:
                        pyxel.text(42 + 37 * x, 42 + 37 * y, str(masu[y][x]), 7)
                    elif masu[y][x] == 2:
                        pyxel.text(42 + 37 * x, 42 + 37 * y, str(masu[y][x]), 3)
                    elif masu[y][x] == 4:
                        pyxel.text(42 + 37 * x, 42 + 37 * y, str(masu[y][x]), 2)
                    elif masu[y][x] == 8:
                        pyxel.text(42 + 37 * x, 42 + 37 * y, str(masu[y][x]), 1)
                    elif masu[y][x] == 16:
                        pyxel.text(42 + 37 * x, 42 + 37 * y, str(masu[y][x]), 4)
                    elif masu[y][x] == 32:
                        pyxel.text(42 + 37 * x, 42 + 37 * y, str(masu[y][x]), 5)
                    elif masu[y][x] == 64:
                        pyxel.text(42 + 37 * x, 42 + 37 * y, str(masu[y][x]), 6)
                    elif masu[y][x] == 128:
                        pyxel.text(38 + 37 * x, 42 + 37 * y, str(masu[y][x]), 8)
                    elif masu[y][x] == 256:
                        pyxel.text(38 + 37 * x, 42 + 37 * y, str(masu[y][x]), 9)
                    else:
                        pyxel.text(38 + 37 * x, 42 + 37 * y, str(masu[y][x]), 0)
        if self.scene == 2:
            pyxel.cls(7)
            pyxel.rect(50, 50, 100, 100, 12)
            pyxel.text(80, 97, "game over", 0)
            pyxel.text(80, 105, ("score:" + str(self.score)), 0)
        if self.scene == 3:
            pyxel.rect(50, 50, 100, 100, 12)
            pyxel.text(80, 97, "game clear", 0)
            pyxel.text(80, 105, ("score:" + str(self.score)), 0)


    def spawn_new_tile(self):
        #新しいタイルを発生させる関数
        # 詰み判定を行い、結果をself.tumi.tumiに格納
        self.tumi.tumi = self.tumi.hanntei(masu)

        # もし詰んでいない場合
        if self.tumi.tumi == 0:
            xx = 0
            # 無限ループ
            while xx == 0:
                # ランダムな位置を選択。これでランダムな位置に生成を行う。
                g = pyxel.rndi(0, 3)
                h = pyxel.rndi(0, 3)

                # 選択した位置が空いているかどうかを確認
                if masu[g][h] == 0:
                    # 空いていたらタイル（2か4）を生成し、ループ終了
                    masu[g][h] = int(pyxel.rndi(11, 20) / 10) * 2
                    xx = 1
        else:
            # もし詰んでいる場合、ゲームオーバーシーンへ遷移し、マウスカーソルを表示
            self.scene = 2
            pyxel.mouse(True)

App()