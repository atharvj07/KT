public class Main{
  public void run(java.io.InputStream in, java.io.PrintStream out){
    java.util.Scanner sc = new java.util.Scanner(in);
    String s;
    char[] c;
    int res, i, l;

    res = 0;
    for(;sc.hasNext();){
      s = sc.next(); c = new char[s.length()];
      for(i = 0;i < s.length();i++)c[i] = s.charAt(i);

      for(i = 0;i < s.length();i++){
        if(c[i] >= '0' && c[i] <= '9'){
          for(l = i;i < s.length() && c[i] >= '0' && c[i] <= '9';)i++;
          res += readint(c, l, i);
        }
      }
    }
    out.println(res);

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