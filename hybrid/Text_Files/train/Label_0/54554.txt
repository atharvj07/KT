import java.util.*;

class P{
  String s;
  int digit;
  boolean re;

  public P(String s,int digit,boolean re){
    this.s = s;
    this.digit = digit;
    this.re = re;
  }

  public String toString(){
    return String.format("[%s, %d, %b]",s,digit,re);
  }
}

public class Main{
  static int n;
  static HashMap<String,Stack<Integer>> map;
  static P[] p;

  public static void Ichi(int idx){
    int now = 1;
    int popIdx = -1;
    Stack<Integer> st = new Stack<Integer>();

    while(!map.get(p[idx].s).isEmpty()){
      popIdx = map.get(p[idx].s).pop();
      if(now + 1 != p[popIdx].digit){
        map.get(p[idx].s).push(popIdx);
        popIdx = -1;
        break;
      }
      System.out.println(popIdx+1);
      st.push(popIdx);
      now++;
    }

    while(!st.isEmpty()){
      int p = st.pop();
      Re(p);
    }
  }

  public static void Re(int idx){
    for(int j=idx-1;j>=0 && p[j].re;j--){
      System.out.println(j+1);
      if(p[j].digit == 1){
        Ichi(j);
      }
    }
  }

  public static void solve(){
    for(int i=0;i<n;i++){
      if(p[i].s.equals("-")){
        System.out.println(i+1);
        Re(i);
        continue;
      }
      if(p[i].digit >= 2){
        map.get(p[i].s).push(i);
        continue;
      }
      if(p[i].re){
        continue;
      }

      System.out.println(i+1);

      if(p[i].digit == 1){
        Ichi(i);
      }

      Re(i);
    }
  }

  public static void main(String[] args){
    Scanner sc = new Scanner(System.in);

    while(true){
      n = sc.nextInt();
      if(n == 0) break;

      map = new HashMap<String,Stack<Integer>>();
      p = new P[n+2];

      for(int i=0;i<n;i++){
        String s = sc.next();
        p[i] = new P("",-1,false);

        if(s.endsWith("v")){
          p[i].re = true;
          s = s.substring(0,s.length()-1);
        }

        int idx = s.length() - 1;
        for(;idx>=0 && '0' <= s.charAt(idx) && s.charAt(idx) <= '9';idx--);

        if(idx != s.length() - 1){
          p[i].digit = Integer.parseInt(s.substring(idx+1));
          s = s.substring(0,idx+1);
        }

        p[i].s = s;
        if(!p[i].s.equals("")){
          map.put(p[i].s,new Stack<Integer>());
        }
      }

      solve();
    }
  }
}