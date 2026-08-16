import java.util.Scanner;

/**
 * Created by jouke on 8/23/15.
 */
public class CF_549A {

  public static void main(String[] args) {
    try (Scanner s = new Scanner(System.in)) {
      int h = s.nextInt();
      int w = s.nextInt();

      byte[][] picture = new byte[h][w];

      for (int i = 0; i < h; i++) {
        String line = s.next();
        for (int j = 0; j < w; j++) {
          switch(line.charAt(j)) {
            case 'f':
              picture[i][j] = 1;
              break;
            case 'a':
              picture[i][j] = 2;
              break;
            case 'c':
              picture[i][j] = 4;
              break;
            case 'e':
              picture[i][j] = 8;
              break;
          }
        }
      }

      int faceCount = 0;

      for (int i = 0; i < h - 1; i++) {
        for (int j = 0; j < w - 1; j++) {
          if ((picture[i][j] | picture[i+1][j] | picture[i][j+1] | picture[i+1][j+1]) == 15) {
            faceCount++;
          }
        }
      }

      System.out.println(faceCount);
    }
  }
}
