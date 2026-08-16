import java.util.Arrays;
import java.util.Scanner;


public class Algorithm {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        
        String line = sc.nextLine();
        
        int[][] xyzi = new int[line.length() + 1][3];
        
        for (int i = 1; i <= line.length(); i++) {
            xyzi[i] = xyzi[i-1].clone();
            char c = line.charAt(i - 1);
            switch (c) {
            case 'x':
                xyzi[i][0]++;
                break;
            case 'y':
                xyzi[i][1]++;
                break;
            case 'z':
                xyzi[i][2]++;
                break;
            }
        }

        int ntests = sc.nextInt();
        
        for (int i = 0; i < ntests; i++) {
            int l = sc.nextInt();
            int r = sc.nextInt();
            
            int x = xyzi[r][0] - xyzi[l - 1][0];
            int y = xyzi[r][1] - xyzi[l - 1][1];
            int z = xyzi[r][2] - xyzi[l - 1][2];
            
            int min = x;
            int max = x;
            min = Math.min(min, y);
            min = Math.min(min, z);
            max = Math.max(max, y);
            max = Math.max(max, z);
            
            if (r - l + 1 < 3) {
                System.out.println("YES");
                continue;
            }
            
            if ((max - min <= 1) && (min > 0)) {
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }
        }
    }
}
