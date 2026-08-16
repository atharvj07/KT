import java.util.*;

class Main{

    int n, m, sz;
    char[] kakko;
    int[] a, bkt, add;

    void solve(){
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        m = sc.nextInt();
        kakko = sc.next().toCharArray();

        sz = Math.max(1, (int)Math.sqrt(n) - 1);
        a = new int[n];
        bkt = new int[n/sz+10];
        add = new int[n/sz+10];
        TreeSet<Integer> set = new TreeSet<Integer>();

        for(int i=0; i<n; i++){
            if(i==0) a[i] = 1;
            else{
                if(kakko[i]=='(') a[i] = a[i-1] + 1;
                else{
                    a[i] = a[i-1] - 1;
                    set.add(i);
                }
            }
            bkt[i/sz] = Math.min(a[i], bkt[i/sz]);
        }

        for(int i=0; i<m; i++){
            int q = sc.nextInt()-1;
            int idx = 0;
            if(kakko[q]=='('){
                kakko[q] = ')';
                set.add(q);
                add(q, n, -2);
                //idx = set.higher(new Integer(-1));
                idx = set.pollFirst();
                kakko[idx] = '(';
                set.remove(idx);
                add(idx, n, 2);
            }else{
                kakko[q] = '(';
                set.remove(q);
                add(q, n, 2);
                idx = search(q);
                kakko[idx] = ')';
                add(idx, n, -2);
                set.add(idx);
            }
            //System.out.println(Arrays.toString(kakko));
            System.out.println(idx+1);
        }
    }

    void add(int start, int last, int num){
        int from = start - start%sz;
        int to = from + sz;
        for(int i=start/sz; i * sz <=last; i++){
            if(start<=from && to<=last){
                add[i] += num;
            }else{
                for(int j=Math.max(from, start); j<to && j<last; j++){
                    a[j] += num;
                }
                int min = Integer.MAX_VALUE;
                for(int j=from; j<to && j<a.length; j++){
                    min = Math.min(min, a[j]);
                }
                bkt[i] = min;
            }
            from = to;
            to += sz;
        }
    }

    int search(int f){        
        int from = f - f%sz;
        int to = from + sz;
            
        for(int i=f/sz; i>=0; i--){
            if(bkt[i]+add[i]<=1){
                for(int j=Math.min(f-1, to-1); j>=from; j--){
                    if(a[j]+add[i]==1) return j+1;
                }
            }
            to = from;
            from -= sz;
        }
        return 0;
    }

    public static void main(String[] args){
        new Main().solve();
    }
}