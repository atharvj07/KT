import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner in = new Scanner(System.in);
        
        while (in.hasNextLine()) {
            int R = in.nextInt();
            int C = in.nextInt();
            if (R == 0 && C == 0) break;
            
            HashMap<Character, Loc> hm = new HashMap<Character, Loc>();
            
            for (int i = 0; i < R; i++) {
                String str = in.next();
                for (int j = 0; j < C; j++) {
                    char c = str.charAt(j);
                    if (c == '_') continue;
                    hm.put(c, new Loc(i, j));
                }
            }
            
            String str = in.next();
            
            int iPos = 0;
            int jPos = 0;
            int count = str.length();
            for (int i = 0; i < str.length(); i++) {
                Loc loc = hm.get(str.charAt(i));
                count += Math.abs(iPos - loc.i) + Math.abs(jPos - loc.j);
                iPos = loc.i;
                jPos = loc.j;
            }
            
            System.out.println(count);
        }
    }
    
    public static class Loc {
        int i;
        int j;
        
        public Loc(int i, int j) {
            this.i = i;
            this.j = j;
        }
    }
}

