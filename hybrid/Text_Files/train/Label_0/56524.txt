import java.util.*;

class Main{

    String[][] ab;

    void solve(){
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        while(n!=0){
            ab = new String[n][2];
            for(int i=0; i<n; i++){
                ab[i][0] = sc.next();
                ab[i][1] = sc.next();
            }
            String start = sc.next();
            String goal = sc.next();

            System.out.println(bfs(start, goal));
            n = sc.nextInt();
        }
    }

    class P{
        String s;
        int cnt;
        P(String s, int cnt){
            this.s = s;
            this.cnt = cnt;
        }
    }

    int bfs(String start, String goal){
        LinkedList<P> list = new LinkedList<P>();
        list.add(new P(start, 0));
        HashSet<String> set = new HashSet<String>();

        while(list.size()>0){
            P p = list.poll();
            String s = p.s; int cnt = p.cnt;

            if(s.length()>=100) continue;
            if(s.equals(goal)) return cnt;
            if(!set.add(s)) continue;

            for(int i=0; i<ab.length; i++){
                String a = ab[i][0];
                String b = ab[i][1];
                String news = s.replaceAll(a, b);
                list.add(new P(news, cnt+1));
            }
        }
        return -1;
    }

    public static void main(String[] args){
        new Main().solve();
    }
}