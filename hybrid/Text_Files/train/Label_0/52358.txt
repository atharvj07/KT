/**
 * Created by vinayr on 10/7/17.
 */
import java.util.*;
public class Code846A {
    public  static  void main(String [] args){
        int n=0;
        Scanner sc = new Scanner(System.in);
        n=sc.nextInt();
        Map<Integer,Integer> mp = new HashMap<>();
        Set<Integer>st = new HashSet<>();
        for(int i=0;i<n;i++){
            int val=0;
            val=sc.nextInt();
            mp.put(val,mp.getOrDefault(val,0)+1);
            st.add(val);
        }
        if(st.size() != 2)
        {
            System.out.println("NO");
        }
        else{
            List<Integer>lst = new ArrayList<>();
            for(Integer i : st){
                lst.add(i);
            }
            int cnt1=mp.get(lst.get(0));
            int cnt2=mp.get(lst.get(1));
            if(cnt1==cnt2){
                System.out.println("YES");
                System.out.println(lst.get(0)+" "+lst.get(1));
            }
            else{
                System.out.println("NO");
            }
        }
    }
}
