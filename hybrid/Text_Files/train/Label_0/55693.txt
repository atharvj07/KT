import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] x = new int[n];
        int[] y = new int[n];
        int[] h = new int[n];
        for(int i=0; i<n; i++) {
            x[i] = in.nextInt();
            y[i] = in.nextInt();
            h[i] = in.nextInt();
        }
        boolean ok = false;
        int ans_x = -1;
        int ans_y = -1;
        int ans_h = -1;
        for(int cy = 0; cy <= 100; cy++) {
            for(int cx = 0; cx <= 100; cx++) {
                ok = true;
                int H = -1;
                for(int i=0; i<n; i++) {
                    if(h[i]==0) {
                        continue;
                    }
                    if(H==-1) {
                        H = h[i] + Math.abs(cx-x[i]) + Math.abs(cy-y[i]);
                    }
                    else if(H == h[i] + Math.abs(cx-x[i]) + Math.abs(cy-y[i])) {
                        continue;
                    }
                    else {
                        ok = false;
                        break;
                    }
                }
                for(int i=0; i<n; i++) {
                    if(h[i]!=0) {
                        continue;
                    }
                    if(H - Math.abs(cx-x[i]) - Math.abs(cy-y[i]) > 0) {
                        ok = false;
                        break;
                    }
                }
                if(ok) {
                    ans_x = cx;
                    ans_y = cy;
                    ans_h = H;
                    break;
                }
            }
            if(ok) {
                break;
            }
        }
        System.out.print(ans_x);
        System.out.print(' ');
        System.out.print(ans_y);
        System.out.print(' ');
        System.out.print(ans_h);
        System.out.println();
    }
}
