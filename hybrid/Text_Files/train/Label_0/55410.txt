import java.util.Scanner;
public class A{
    public static void main(String[] args) {
        Scanner sObj = new Scanner(System.in);
        int css = sObj.nextInt();
        for(int zz=0; zz<css; zz++){
            int x1 = sObj.nextInt();
            int y1 = sObj.nextInt();
            int x2 = sObj.nextInt();
            int y2 = sObj.nextInt();
            int diff1 = Math.abs(x1-x2);
            int diff2 = Math.abs(y1-y2);
            if(diff1 == 0 || diff2 == 0) System.out.println(diff1 + diff2);
            else System.out.println(diff1 + diff2 + 2);
        }
    }
}