import java.io.*;
import java.util.*;

public class Main {
    //    static PrintWriter out = new PrintWriter(System.out);
    static Scanner sc = new Scanner(System.in);
    static BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    public static void main(String[] args) throws IOException {
        Main main = new Main();
        String ans = main.solve();
        System.out.println(ans);
    }
    String solve() throws IOException{
        int n = sc.nextInt();
        // ascending of Ai
        PriorityQueue<Pair> front = new PriorityQueue<>(100,(o1,o2)->(o1.A-o2.A));
        // descending of Bi
        PriorityQueue<Pair> back = new PriorityQueue<>(100,(o1,o2)->(o2.B-o1.B));
        int perfect = 0;
        for(int i=0;i<n;i++){
            String s = sc.next();
            int[] temp = helper(s);
            if(temp[0]==0&&temp[1]==0) {
                perfect ++;
                continue;
            }
            Pair p = new Pair(temp[0],temp[1]);
            if(temp[0]==0||p.B>=p.A) front.add(p);
            else back.add(p);
        }
        if(perfect>0&&front.size()==0) {
            perfect--;
            front.add(new Pair(0,0));
        }
        while(perfect-->0) back.add(new Pair(0,0));
        ArrayList<Pair> list = new ArrayList<>();
        while(front.size()>0) list.add(front.poll());
        while(back.size()>0) list.add(back.poll());
        int left = 0, right = 0;
        for(int i=0;i<list.size();i++){
            Pair p = list.get(i);
            if(left-p.A<0) return "No";
            left += p.B-p.A;
        }
        for(int i=list.size()-1; i>=0; i--){
            Pair p = list.get(i);
            if(right-p.B<0) return "No";
            right += p.A-p.B;
        }
        if(left==0&&right==0) return "Yes";
        else return "No";

    }
    int[] helper(String s){
        int[] ans = new int[2];
        char[] arr = s.toCharArray();
        int mini = 100, left = 0, right = 0;
        for(char c:arr){
            if(c=='(') left++;
            else left--;
            mini = Math.min(mini,left);
        }
        ans[0] = Math.abs(Math.min(mini,0));
        mini = 100;
        for(int i=arr.length-1;i>=0;i--){
            if(arr[i]==')') right++;
            else right--;
            mini = Math.min(mini, right);
        }
        ans[1] = Math.abs(Math.min(mini,0));
        return ans;
    }
    class Pair{
        int A, B;
        // means ")"*A + "("*B
        public Pair(int _A, int _B){A=_A;B=_B;}
    }
}