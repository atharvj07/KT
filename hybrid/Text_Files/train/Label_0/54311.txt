import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    ;
    static String currentInputLine = "";
    static int currentInputIndex = 0;

//    public FastScanner(String fileName) throws FileNotFoundException {
//        reader = new BufferedReader(new InputStreamReader(new FileInputStream(fileName)));
//    }

    static void nextInputLine() {
        try {
            currentInputLine = reader.readLine();
            currentInputIndex = 0;
        } catch (IOException ignored) {
            throw new RuntimeException();
        }
    }

    static void skipSpaces() {
        if (currentInputLine == null) {
            return;
        }
        while (currentInputIndex < currentInputLine.length() && currentInputLine.charAt(currentInputIndex) == ' ') {
            currentInputIndex++;
        }
        if (currentInputIndex == currentInputLine.length()) {
            nextInputLine();
            skipSpaces();
        }
    }

    static boolean hasNext() {
        skipSpaces();
        return currentInputLine != null;
    }

    static String next() {
        skipSpaces();
        int end = currentInputLine.indexOf(" ", currentInputIndex);
        if (end == -1) {
            end = currentInputLine.length();
        }
        String res = currentInputLine.substring(currentInputIndex, end);
        currentInputIndex = end;
        return res;
    }

    static int nextInt() {
        return Integer.parseInt(next());
    }

    static long nextLong() {
        return Long.parseLong(next());
    }

    static float nextFloat() {
        return Float.parseFloat(next());
    }

    static double nextDouble() {
        return Double.parseDouble(next());
    }

    private static void solve() {
        int n = nextInt();
        int k = nextInt();
        String s = next();
        if (n % k != 0) {
            System.out.println(-1);
            return;
        }
        TreeMap<Character, Integer> charMap = new TreeMap<>();
        int diff = 0;
        int maxPrefLen = -1;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) != 'z' && (s.length() - i >= diff && charMap.higherKey(s.charAt(i)) != null ||
                    s.length() - i - k >= diff
            )) {
                maxPrefLen = i;
            }

            charMap.merge(s.charAt(i), k - 1, (old, nw) -> (old - 1 + k) % k);
            if (charMap.get(s.charAt(i)) == k - 1) {
                diff += k - 1;
            } else {
                diff--;
            }
            if (charMap.get(s.charAt(i)) == 0) {
                charMap.remove(s.charAt(i));
            }
        }
        if (diff == 0) {
            System.out.println(s);
            return;
        }
        if (maxPrefLen == -1) {
            System.out.println(-1);
            return;
        }
        charMap = new TreeMap<>();
        diff = 0;
        for (int i = 0; i < maxPrefLen; i++) {
            charMap.merge(s.charAt(i), k - 1, (old, nw) -> (old - 1 + k) % k);
            if (charMap.get(s.charAt(i)) == k - 1) {
                diff += k - 1;
            } else {
                diff--;
            }
            if (charMap.get(s.charAt(i)) == 0) {
                charMap.remove(s.charAt(i));
            }
        }
        if (charMap.higherKey(s.charAt(maxPrefLen)) == null || charMap.higherKey(s.charAt(maxPrefLen)) - s.charAt(maxPrefLen) > 1 && s.length() - maxPrefLen - k >= diff) {
            charMap.put((char) (s.charAt(maxPrefLen) + 1), k);
            diff += k;
        }
        StringBuilder result = new StringBuilder();
        result.append(s, 0, maxPrefLen);
        result.append(charMap.higherKey(s.charAt(maxPrefLen)));
        charMap.merge(charMap.higherKey(s.charAt(maxPrefLen)), 1, (old, nw) -> old - 1);
        diff--;
        result.append("a".repeat(s.length() - maxPrefLen - 1 - diff));
        for (char c : charMap.keySet()) {
            result.append(String.valueOf(c).repeat(charMap.get(c)));
        }
        System.out.println(result);
    }

    public static void main(String[] args) {
        int t = nextInt();
        for (int i = 0; i < t; i++) {
            solve();
        }
    }
}
