pocpkhc殿のforkリポジトリ

# 最適化アルゴリズム(主にメタヒューリスティクス)の実装コード
以下Qiita記事の実装コードとなります。
コードの解説については記事を参照してください。

+ [最適化アルゴリズムを実装していくぞ（概要）](https://qiita.com/pocokhc/items/07b698cc426cadb3a64e)


# 実装アルゴリズム

+ 遺伝的アルゴリズム(Genetic Algorithm: GA)
+ 実数型遺伝的アルゴリズム
  + GA BLX-α
  + GA SPX
+ 人口蜂コロニーアルゴリズム(Artificial Bee Colony: ABC)
+ 粒子群最適化(Particle Swarm Optimization: PSO)
+ ホタルアルゴリズム(Firefly Algorithm)
+ コウモリアルゴリズム(Bat Algorithm)
+ カッコウ探索(Cucko Search)
+ ハーモニーサーチ(Harmony Search)
+ くじらさんアルゴリズム(The Whale Optimization Algorithm: WOA)
+ 差分進化(Differential Evolution: DE)
+ タブーサーチ(Tabu Search)

# 実装問題

+ OneMax問題
+ 巡回セールスマン問題(Traveling Salesman Problem: TSP)
+ エイト・クイーン(Eight Queens)
+ ライフゲーム
+ 2048
+ [最適化アルゴリズムを評価するベンチマーク関数まとめ](https://qiita.com/tomitomi3/items/d4318bf7afbc1c835dda)より
  + Ackley function
  + Griewank function
  + Michalewicz function
  + Rastrigin function
  + Schwefel function
  + Styblinski-Tang function
  + Xin-She Yang function


# Getting started
## 1. pip install
使っているパッケージは以下です。

+ pip install numpy
+ pip install matplotlib
+ pip install joblib
+ pip install pandas
+ pip install optuna


## 2. download
このレポジトリをダウンロードします。

``` bash
> git clone https://github.com/pocokhc/metaheuristics.git
```

## 3. Run the program
examples にいくつか実行例が入っています。

``` bash
> cd metaheuristics/examples

# 全問題と全アルゴリズムに対して探索を実行します
> python main.py

# 1次元と2次元を設定できる問題について、各アルゴリズムの探索過程をgif出力します
> python train_plot.py

# 1次元と2次元を設定できる問題について、結果を画像出力します
> python function_plot.py

# TSPを簡単に探索した結果を出力します
> python plot_TSP.py

```



