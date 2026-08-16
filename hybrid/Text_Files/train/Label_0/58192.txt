import java.util.*;

class Main{

    boolean check(){
        Scanner sc = new Scanner(System.in);
        Pair[] D = new Pair[6];

        for ( int i = 0; i < 6; i++ ) {
            D[i] = new Pair(0, 0);
            D[i].first = sc.nextInt();
            D[i].second = sc.nextInt();
            if ( D[i].first > D[i].second) {
                int tmp = D[i].first;
                D[i].first = D[i].second;
                D[i].second = tmp;
            }
        }
        Arrays.sort(D, new Comparator<Pair>(){
                public int compare(Pair a, Pair b){
                    if ( a.first == b.first ) return a.second - b.second;
                    return a.first - b.first;
                }
            });
        for ( int i = 0; i < 6; i+=2){
            if ( D[i].first == D[i+1].first && D[i].second == D[i+1].second ) D[i/2] = D[i];
            else return false;
        }

        return D[0].first == D[1].first && D[0].second == D[2].first && D[1].second == D[2].second;
    }

    void solve(){
        if ( check() ) System.out.println("yes");
        else System.out.println("no");
    }

    class Pair{
        public int first;
        public int second;

        Pair (int first, int second) {
            this.first = first;
            this.second = second;
        }
    }

    public static void main(String[] args){ new Main().solve(); }
}


