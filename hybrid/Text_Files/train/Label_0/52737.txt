import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class E172 {

    public static void main(String[] args) throws Exception {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(System.out);

        Parser parser = new Parser(in.readLine());
        List<Token> list = new ArrayList<Token>();
        
        while (true) {
            Token s = parser.next();
            if (s == null) break;
            list.add(s);
        }
        
        int[] st = new int[N+1], st1 = new int[MAX+1];
        int sp = 0, sp1 = 0;
        
        int n = Integer.valueOf(in.readLine());
        L : for (int cs = 0; cs < n; cs++) {
            String[] t = in.readLine().split(" ");
            int k = t.length;
            int[] v = new int[k];
            for (int i = 0; i < k; i++) {
                if (!map.containsKey(t[i])) {
                    out.println(0);
                    continue L;
                }
                v[i] = map.get(t[i]);
            }
            
            int ans = 0, id = 0;
            sp = 0;
            sp1 = 0;
            for (Token tk : list) {
                if (tk.type == 1) {
                    if (tk.hash == v[sp]) {
                        if (sp == k-1) ans++;
                        else {
                            st[sp++] = id;
                        }
                    }
                    st1[sp1++] = id++;
                }
                else if (tk.type == 2) {
                    sp1--;
                    if (sp > 0 && st1[sp1] == st[sp-1]) sp--;
                }
                else if (tk.type == 3) {
                    if (tk.hash == v[sp]) {
                        if (sp == k-1) ans++;
                    }
                }
            }
            
            out.println(ans);
        }
        
        out.flush();
    }
    
    static final int MAX = 1000000, N = 200;
    static Map<String, Integer> map = new HashMap<String, Integer>(MAX);

    static class Parser {
        String s;
        int p = 0;
        
        Parser(String s) {
            this.s = s;
        }
        
        Token next() {
            String res = "";
            p++;
            if (p >= s.length()) return null;
            while (s.charAt(p) != '>') {
                res += s.charAt(p++);
            }
            int type = 1;
            if (res.charAt(0) == '/') {
                type = 2;
                res = res.substring(1);
            }
            else if (res.charAt(res.length()-1) == '/') {
                type = 3;
                res = res.substring(0, res.length()-1);
            }
            p++;
            
            return new Token(res, type);
        }
    }
    
    static class Token {
        int hash;
        int type;
        
        Token(String str, int type) {
            if (!map.containsKey(str)) map.put(str, map.size());
            this.hash = map.get(str);
            this.type = type;
        }
    }
}
