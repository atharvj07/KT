import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner fs = new Scanner(System.in);
        int n = fs.nextInt();
        long[] inp = new long[n];
        for(int i=0 ; i<n ; i++){
            inp[i] = fs.nextLong();
        }

        int ans = 0 ;

        for(int i=0 ; i<n ; i++){
            for(int j=i+1 ; j<n ; j++){
                if(inp[i]==inp[j]){
                    continue;
                }
                for(int k= j+1 ; k<n ; k++){
                    if(inp[k]==inp[i] || inp[k]==inp[j]){
                        continue;
                    }else{
                        long a = inp[i];
                        long b = inp[j];
                        long c = inp[k];
                        if((a+b > c) && (b+c>a) && (c+a>b)){
                            ans++;
                        }
                    }
                }
            }
        }

        System.out.println(ans);

    }
}
