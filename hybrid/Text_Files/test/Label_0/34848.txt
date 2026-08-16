import java.io.*;
import java.util.Scanner;
import java.util.Arrays;

public class MyCode {
  public static void main (String[] args) {
    Scanner sc = new Scanner(System.in);
    
    int n = sc.nextInt();
    int m = sc.nextInt();
    int[] bookPerGenre = new int[m];
    
    Arrays.fill(bookPerGenre, 0);
    
    for (int i = 0; i < n; i++){
      int genre = sc.nextInt();
      bookPerGenre[genre-1]++;
    }
    int sum = 0;
    
    for (int i = 0; i < m; i++){
      for (int j = i + 1; j < m; j++){
        sum += bookPerGenre[i]*bookPerGenre[j];
      }
    }
    
    System.out.println(sum);
    
//     a, b
//     0, b => distance = |0 - b|
//     n - 1, b  => | n - 1 - b |
//     a, 0 => |a - 0|
//     a, n - 1 => |a - (n - 1)|
  }
}