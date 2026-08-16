import java.util.Arrays;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        
        int n = Integer.parseInt(sc.next());
        int q = Integer.parseInt(sc.next());
        
        SegmentTreeRSQ st = new SegmentTreeRSQ(n);
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < q; i++){
            if(sc.next().equals("0")){
                st.add(Integer.parseInt(sc.next()) -1, Integer.parseInt(sc.next()));
            }else{
                sb.append(st.getSum(Integer.parseInt(sc.next()) -1, Integer.parseInt(sc.next()), 0, 0, st.n));
                sb.append(System.lineSeparator());
            }
        }
        System.out.print(sb);
    }
    
    static class SegmentTreeRSQ {
        int n;
        int[] node;

        public SegmentTreeRSQ(int size) {
            n = 1;
            while(n < size) n <<= 1;
            node = new int[2*n-1];
            Arrays.fill(node, 0);
        }
        void add(int i, int x){
            i += n-1;
            node[i] += x;
            while(i > 0){
                i = (i-1)/2;
                node[i] = node[i*2+1] + node[i*2+2];
            }
        }
        int getSum(int a, int b, int k, int l, int r){
            if(r <= a || b <= l) return 0;
            if(a <= l && r <= b){
                return node[k];
            }else{
                int vl = getSum(a, b, k*2+1, l, (l+r)/2);
                int vr = getSum(a, b, k*2+2, (l+r)/2, r);
                return vl + vr;
            }
        }
    }
}
