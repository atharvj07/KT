import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int q = scan.nextInt();
        scan.nextLine();

        for (int i = 0; i < q; i++) {
            handleQ(scan);
        }
    }

    private static void handleQ(Scanner scan) {
        int n = scan.nextInt();
        ArrayList<Integer> list = new ArrayList<>();

        for (int i = 0; i < 4*n; i++) {
            list.add(scan.nextInt());
        }

        list.sort(Integer::compareTo);

        int iMin = 0;
        int iMax = 4*n-1;
        int area = -1;

        while(iMin < iMax) {
            if(list.get(iMin).equals(list.get(iMin+1)) && list.get(iMax).equals(list.get(iMax-1))) {
                int areaI = list.get(iMin) * list.get(iMax);
                if(area == -1 || area == areaI) {
                    area = areaI;
                } else {
                    System.out.println("NO");
                    return;
                }
                iMin += 2;
                iMax -= 2;
            } else {
                System.out.println("NO");
                return;
            }
        }

        System.out.println("YES");
    }
}