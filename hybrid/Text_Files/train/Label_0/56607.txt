import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        
        int n = Integer.parseInt(sc.next());
        String s = sc.next();
        
        int[] a = new int[n];
        a[0] = 0;
        int b = 0;
        for(int i = 0; i < n-1; i++){
            if(s.charAt(i) == 'W'){
                b++;
            }
            a[i+1] = b;
        }
        
        int[] c = new int[n];
        c[n-1] = 0;
        int d = 0;
        for(int i = n-1; i > 0; i--){
            if(s.charAt(i) == 'E'){
                d++;
            }
            c[i-1] = d;
        }
        
        int min = 1000000;
        int e;
        for(int i = 0; i < n; i++){
            e = a[i] + c[i];
            if(e < min){
                min = e;
            }
        }
        
        System.out.println(min);
    }
}