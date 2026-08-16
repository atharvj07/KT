//  20/8/20  12:14 PM  Aug  2020
import java.util.*;
public class _239A {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long y=sc.nextLong();
        long k=sc.nextLong();
        long n=sc.nextLong();
        StringBuilder st= new StringBuilder();
        long i=k-y%k;
        while(i+y<=n){
                st.append(i).append(" ");
                i += k;
        }
        System.out.println(st.length()==0?"-1":st);
    }
}