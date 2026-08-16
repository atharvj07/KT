import java.util.*;
import java.lang.*;

class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int cx1 = scanner.nextInt();
        int cy1 = scanner.nextInt();
        int r1 = scanner.nextInt();
        int cx2 = scanner.nextInt();
        int cy2 = scanner.nextInt();
        int r2 = scanner.nextInt();
        
        // Calculate distance between two centers
        double dist = Math.sqrt(Math.pow(cx1-cx2,2) + Math.pow(cy1-cy2,2));
        
        int sum_r = r1 + r2;
        int dif_r = Math.abs(r1 - r2);
        
        if(sum_r < dist) System.out.println(4);
        else if(sum_r == dist) System.out.println(3);
        else if(dif_r < dist && dist < sum_r) System.out.println(2);
        else if(dist == dif_r) System.out.println(1);
        else if(dist < dif_r) System.out.println(0);
    }
}
