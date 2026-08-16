import java.util.Scanner;

public class B {
    public static void main(String args[]){
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int b[][] = new int[1000001][3];
        int max = 0 , l = 0 , r = 0;
        for(int i = 0 ; i < n ; i++){
            int t = in.nextInt();
            if(b[t][0]==0){
                b[t][0]++;
                b[t][1] = i+1;
                if(b[t][0]>max){
                    l=r=i+1;
                    max=b[t][0];
                }
            }else{
                b[t][0]++;
                b[t][2]=i+1;
                if(b[t][0]>max||(b[t][0]==max&&r-l>b[t][2]-b[t][1])){
                    l= b[t][1];
                    r = b[t][2];
                    max=b[t][0];
                }
            }
        }
        System.out.println(l+" "+r);
    }
}
