import java.util.*;

public class Main {
    static int n;
    static int[] bit;

    static void add(int x, int y) {
        for (int i=x;i<=n;i+=i&(-i)) {
            bit[i]+=y;
        }
    }

    static int sum(int x) {
        int tmp = 0;
        for (int i=x;i>0;i-=i&(-i)) {
            tmp+=bit[i];
        }
        return tmp;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        char[] c = s.toCharArray();
        n = s.length();
        bit = new int[n+1];
        int k = sc.nextInt();

        ArrayList<ArrayDeque<Integer>> list = new ArrayList<ArrayDeque<Integer>>();
        for (int i=0;i<26;i++) {
            ArrayDeque<Integer> add = new ArrayDeque<Integer>();
            list.add(add);
        }
        for (int i=0;i<n;i++) {
            list.get((int)c[i]-97).addLast(i);
            add(i+1, 1);
        }


        StringBuilder sb = new StringBuilder();
        for (int i=0;i<n;i++) {
            for (int j=0;j<26;j++) {
                if (list.get(j).size()==0) continue;
                int pos = list.get(j).getFirst();
                int cnt = sum(pos);

                if (cnt<=k) {
                    list.get(j).pollFirst();
                    k -= cnt;
                    sb.append((char)(97+j));
                    add(pos+1, -1);
                    break;
                }
            }
        }

        System.out.println(sb);
    }
}
