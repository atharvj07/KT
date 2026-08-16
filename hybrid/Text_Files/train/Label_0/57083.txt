import java.io.BufferedReader;
import java.io.InputStreamReader;


public class A1370 {
    public static void main(String[] args) {
        try{
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            int t = Integer.parseInt(br.readLine());
            while(t--!=0){
                int n = Integer.parseInt(br.readLine());
                System.out.println(n/2);
            }
        }catch (Exception e){

        }
    }
    public static int gcd(int a, int b){
        if(a==0)return b;
        return gcd(b%a,a);
    }
}
