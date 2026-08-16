import java.io.*;
import java.util.*;


/**
 * AIZU ONLINE JUDGE
 * 3112
 *  2020/5/4
 */
public class Main {

    String S;
    String T;
    int k;

    // 部分文字列を表すクラス
    class Str implements Comparable<Str> {
        String str;
        int idx;

        Str(String str, int idx) {
            this.str = str;
            this.idx = idx;
        }

        String getStr() {
            return str.substring(idx);
        }

        int length() {
            return str.length() - idx;
        }

        // for Debug
        public String toString() {
            if (length() > 100) {
                return str.substring(idx, idx + 100) + "...";
            }
            return getStr();
        }

        @Override
        public int compareTo(Str o) {
           int len1 = length();
           int len2 = o.length();
           int lim = Math.min(len1, len2);

           int k = 0;
           while (k < lim) {
               char c1 = str.charAt(idx + k);
               char c2 = o.str.charAt(o.idx + k);
               if (c1 != c2) {
                   return c1 - c2;
               }
               k++;
           }
           return len1 - len2;
       }

    }

    List<Str> dic = new ArrayList<>();

    void createDic() {
        for(int i = 0; i <= T.length() - k; i++) {
            dic.add(new Str(T, i));
        }
        Collections.sort(dic);
    }

    // 先頭から一致する文字数を返す
    int matchNum(Str s1, Str s2) {
        for(int i = 0;; i++) {
            if (i >= s1.str.length() - s1.idx || i >= s2.str.length() - s2.idx
                    || s1.str.charAt(s1.idx + i) != s2.str.charAt(s2.idx + i)) {
                return i;
            }
        }
    }

    // Tに含まれる、Sのidxからの一致する文字数をかえす
    int matchLength(int idx) {
        Str ss = new Str(S, idx);
        int bi = Collections.binarySearch(dic, ss);
        if (bi >= 0)
            return S.length() - idx;
        bi = -bi - 1;

        int ret = 0;

        if (bi - 1 >= 0) {
            ret = matchNum(ss, dic.get(bi - 1));
        }
        if (bi < dic.size()) {
            ret = Math.max(ret, matchNum(ss, dic.get(bi)));
        }
        return ret;
    }


    boolean check() {
        int[] a = new int[S.length()]; // 0:未調査 1:OK 2:調査済
        a[0] = 1;
        int min = 0;
        int max = 0;

        for(;;) {
            int idx;
            if (max >= 0 && a[max] == 1) {
                idx = max;
            }
            else {
                int oldMax = max;
                for(idx = max; idx >= 0; idx--) {
                    if (a[idx] == 1) {
                        max = idx;
                        break;
                    }
                    if (idx < min)
                        break;
                }
                if (idx < min) {
                    return false;
                }
                log.printf("max %d -> %d\n", oldMax, max);
            }
            int len = matchLength(idx);
            log.printf("matchLength(idx = %d) = %d\n", idx, len);
            if (len >= k) {
                if (idx + len == S.length()) {
                    return true;
                }
                if (len >= k * 2) {
                    min = Math.max(min, idx + len - k);
                }
                for(int j = k; j <= len; j++) {
                    if (a[idx + j] == 0) {
                        a[idx + j] = 1;
                        if (max < idx + j) {
                            max = idx + j;
                        }
                    }
                }
                a[idx] = 2; // NG
            }
            else {
                int j;
                for(j = idx; j > idx + len - k; j--) {
                    a[idx] = 2; // NG
                }
                max = j;
            }
        }
    }


    boolean main() throws IOException {

        Scanner sc = new Scanner(systemin);

        S = sc.nextLine();
        log.printf("S(%d) %s\n", S.length(), new Str(S, 0));
        T = sc.nextLine();
        log.printf("T(%d) %s\n", T.length(), new Str(T, 0));
        k = sc.nextInt();
        log.printf("k %s\n", k);

        createDic();

        boolean yes = check();

        result.printf("%s\n", yes ? "Yes" : "No");

        sc.close();
        return false;
    }



    PrintStream log;
    PrintStream result = System.out;
    BufferedReader systemin;

    static Main instance = new Main();

    Main() {
        systemin = new BufferedReader(new InputStreamReader(System.in));
        log = new PrintStream(new OutputStream() { public void write(int b) {} } );
    }

    public static void main(String[] args) throws IOException {

        instance.main();
        instance.systemin.close();
    }


}


