import java.io.*;

public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    
    String[] nm = br.readLine().split(" ");
    int n = Integer.parseInt(nm[0]);
    int m = Integer.parseInt(nm[1]);
    
    String[] data;
    int[][] switchList = new int[m][n];
    int k;
    int temp;
    for (int i=0; i<m; i++){
      data = br.readLine().split(" ");
      k = Integer.parseInt(data[0]);
      for (int j=0; j<k; j++){
        temp = Integer.parseInt(data[1+j]) - 1;
        switchList[i][temp] = 1;
      }
    }
    int[] p = new int[m];
    String[] ps = br.readLine().split(" ");
    int num;
    boolean allOn;
    for (int i=0; i<m; i++){
      p[i] = Integer.parseInt(ps[i]);
    }
    int[] switches = new int[n];
    int result = 0;
    for (int i=0; i<Math.pow(2, n); i++){
      for (int j=0; j<n; j++){
        switches[j] = (i%(int)Math.pow(2, j+1))/(int)Math.pow(2, j);
      }
      allOn = true;
      for (int j=0; j<m; j++){
        num = 0;
        for (int l=0; l<n; l++){
          num += switchList[j][l]*switches[l];
        }
        if (num%2 != p[j]) allOn = false;
      }
      if (allOn) result++;
    }
    System.out.println(result);
  }
}
