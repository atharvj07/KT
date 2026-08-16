public class Main{
  public void run(java.io.InputStream in, java.io.PrintStream out){
    java.util.Scanner sc = new java.util.Scanner(in);
/*answer*/
    int[] l, v;
    int i, j, k, sum;
    String str;
    char[] ch;
    double d;

    l = new int[10]; v = new int[2];
    for(;sc.hasNext();){
      str = sc.next();
      ch = new char[str.length()];
      for(j = 0;j < str.length();j++)ch[j] = str.charAt(j);
      k = 0; j = 0;

      for(i = 0;i < 10;i++){
        for(;j < str.length();j++){
          if(ch[j] == ','){
            l[i] = readint(ch, k, j);
            k = ++j; break;
          }
        }
      }
      for(;j < str.length();j++){
        if(ch[j] == ','){
          v[0] = readint(ch, k, j);
          k = ++j; break;
        }
      }
      v[1] = readint(ch, k, str.length());

      d = 0;
      for(i = 0;i < 10;i++)d += (double)l[i];
      d = d * (double)v[0] / (double)(v[0] + v[1]);

      sum = 0;
      for(i = 0;i < 10;i++){
        sum += l[i];
        if(d <= sum){
          out.println(i + 1);
          break;
        }
      }
    }

    sc.close();
  }
  public static void main(String[] args){
    (new Main()).run(System.in, System.out);
  }
  private static int readint(char[] ch, int l, int r){
    int i, d, res;
    d = 1; res = 0;
    for(i = r - 1;i >= l;i--){
      res += d * (int)(ch[i] - '0');
      d *= 10;
    }
    return res;
  }
}