import java.util.Scanner;
import java.util.ArrayList;

class Main{
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);

    int count = scan.nextInt();

    while(count>0) {
      int[][] arr = new int[count][2];
      for(int i = 0; i < count; i++) {
        char[] input = scan.next().toCharArray();
        //System.out.println(input);
        arr[i][0] = input.length;
        arr[i][1] = input[input.length-1];
      }

      Func.ite = 0;
      Func.arr = arr;

      System.out.println(new Func().calc());

      count = scan.nextInt();
    }
  }
}

class Func{
  static int ite;
  static int[][] arr;
  char mark;
  ArrayList<Func> list;

  Func() {
    mark = (char)arr[ite][1];
    switch(arr[ite][1]) {
      case '+':
      case '*':
        int deep = arr[ite][0];
        ite++;
        list = new ArrayList<>();
        while(ite<arr.length&&arr[ite][0]>deep) {
          list.add(new Func());
        }
        break;
      default:
        ite++;
        break;
    }
  }

  int calc() {
    int sum = 0;
    switch(mark) {
      case '+':
        for(Func _f : list) {
          sum += _f.calc();
        }
        return sum;
      case '*':
        sum = 1;
        for(Func _f : list) {
          sum *= _f.calc();
        }
        return sum;
      default:
        return (int)(mark-'0');
    }
  }
}