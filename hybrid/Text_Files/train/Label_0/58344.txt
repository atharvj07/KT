import java.util.*;
import static java.lang.System.*;
public class Main{
    public static void main(String[]$){
        Scanner sc = new Scanner(in);

        int n=sc.nextInt();
        int m=sc.nextInt();
        int[] a=new int[m+1];
        int[] b=new int[m+1];
        for (int i = 1; i <=m ; i++) {
            a[i] = sc.nextInt();
            b[i] = sc.nextInt();
        }

        int[] node=new int[n+1];
        //頂点1,2,3,...,n
        //探索済み→node[i]=-1,未探索→node[i]=0
        //0はジャマなのではじめから探索済みにしておく
        node[0]=-1;

        //各頂点iに対し、そことつながっている頂点j,k,...をbridge[i]=j,k....で表す
        ArrayList<Integer>[] bridge=new ArrayList[n+1];

        //bridge[i]はそれぞれがリストなのですべて初期化する必要がある（bridge[0]は使わないので放置）
        for (int i = 1; i <=n ; i++) {
            bridge[i]=new ArrayList<>();
        }

        //辺の追加
        //頂点a[i],b[i]につながっている頂点をbridge[a[i]],bridge[b[i]]に追加していく（隣接リスト）
        for(int i=1;i<=m;i++){
            bridge[a[i]].add(b[i]);
            bridge[b[i]].add(a[i]);
        }

        int ans=0;

        //全探索
        for (int i = 1; i <=m; i++) {
            //i番目の辺を削除
            //Integerにキャストしないと「a[i]番目の要素を削除」となってしまいぬるぽを吐く
            bridge[a[i]].remove((Integer)b[i]);
            bridge[b[i]].remove((Integer)a[i]);
            //条件を満たすか確認（BFSでグラフが連結か判定）満たすなら++ans
            if(bfs(node,bridge))++ans;
            //i番目の辺を復元
            bridge[a[i]].add(b[i]);
            bridge[b[i]].add(a[i]);
        }

        out.println(ans);
    }
    //グラフをBFS（Queueを用いる）
    static boolean bfs(int[] node,ArrayList[] x){
        Queue<Integer> q=new ArrayDeque<>();

        //node[]の添え字は0～nなので配列長はn+1、よってnはnode[]の配列長-1
        int n=node.length-1;

        //初期化（全頂点を未探索にする）
        for(int i=1;i<=n;i++){
            node[i]=0;
        }

        //未探索→探索済みの回数（新たに到達した頂点の個数）をカウント(新たに頂点を探索したら++sum)
        //つまり、sumは「到達することができた頂点の個数」である
        //もし全体が連結ならば最終的にsum==nとなるはず
        int sum=0;

        //頂点1から探索開始
        q.add(1);

        //BFS
        while(q.size()>0) {
            int tempnode = q.poll();
            //未探索かどうか判定
            if (node[tempnode] == 0) {
                //探索済みにする
                node[tempnode] = -1;
                //新たに到達したので++sum
                ++sum;
                //隣接する頂点をQueueに入れる（BFSですね）
                for (Object k : x[tempnode]) {
                    q.add((Integer) k);
                }
            }
        }

        //グラフが非連結になっているかどうか判定（非連結になっていれば題意を満たします）
        return sum!=n;
    }
  //最後までお読みいただき、誠にありがとうございます。
}