import java.util.Scanner;

public class APRILFOOLB {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        int[] arr = new int[n];
        for(int i = 0;i<n;i++){
            arr[i] = s.nextInt();
        }
        boolean bool =false;
        for(int i = 0;i<n-1;i++){
            if(Math.abs(arr[i] - arr[i+1]) >= 2){
                bool = true;
                break;
            }
        }
        if(bool){
            System.out.println("NO");
        }else{
            System.out.println("YES");
        }
    }
}
