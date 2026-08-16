//package codeforce.a20j.under1300;

import java.util.Scanner;

/**
 * @author pribic (Priyank Doshi)
 * @since 20/02/21
 */
public class practiceunder1300 {

  public static void main(String[] args) {
    try (Scanner sc = new Scanner(System.in)) {
      int T = 1;
      //sc.nextInt();
      int ans = 0;
      for (int tt = 1; tt <= T; tt++) {
        String borze = sc.next();
        StringBuilder num = new StringBuilder();
        for (int i = 0; i < borze.length(); i++) {
          switch (borze.charAt(i)) {
            case '.':
              num.append('0');
              break;
            case '-':
              num.append(borze.charAt(i + 1) == '-' ? '2' : '1');
              i++;
              break;

          }
        }
        System.out.println(num.toString());
      }
    }
  }
}

// 0, 0 , new origin -5,3 -> 5+5, 3-3 means i have to do +5, -3 from each cordinate 