import java.util.*;

public class Main {

  public static void main (String[] args) {

    Scanner sc = new Scanner(System.in);

    int N = sc.nextInt();
    int[][] red = new int[N][3];
    int[][] blue = new int[N][3];

    for (int i = 0; i < N; i++) {
      red[i][0] = sc.nextInt();
      red[i][1] = sc.nextInt();
      red[i][2] = 0;
    }

    for (int i = 0; i < N; i++) {
      blue[i][0] = sc.nextInt();
      blue[i][1] = sc.nextInt();
      blue[i][2] = 0;
    }

    sc.close();

    int count = 0;

    Arrays.sort(red, (a,b) -> Integer.compare(a[1],b[1]));
    Arrays.sort(blue, (a,b) -> Integer.compare(a[0],b[0]));

    for (int i = 0; i < N; i++) {
      for (int j = N-1; 0 <= j; j--) {
        if (red[j][2] == 0 && blue[i][2] == 0) {
          if (red[j][0] < blue[i][0] && red[j][1] < blue[i][1]) {
            red[j][2] = 1;
            blue[i][2] = 1;
            count++;
          }
        }
      }
    }

    System.out.println(count);

  }

}