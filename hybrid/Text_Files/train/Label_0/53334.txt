import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map.Entry;
import java.util.StringTokenizer;

public class Round65_E {

    ArrayList<Integer> g[];

    int N, K;
    int[] input;
    int[] target;
    HashMap<String, Integer> hash;
    HashMap<Integer, String> antiHash;

    int memo[][];

    final int TRUE = 1, FALSE = 0;

    int[] ans;

    int[] simpleMask;
/*
17 11
He He He He He He He He He He He He He He He He He
He He He He He He He He S H H

*/
    public boolean go(int index, int mask) {

        if (index == K)
            return mask == (1 << N) - 1;
        if (memo[index][simpleMask[mask]] != -1)
            return memo[index][simpleMask[mask]] == TRUE;
        for (int subset : g[target[index]]) {
            if ((subset & mask) == 0 && go(index + 1, mask | subset)) {
                memo[index][simpleMask[mask]] = TRUE;
                ans[index] = subset;
                return true;
            }
        }
        memo[index][simpleMask[mask]] = FALSE;
        return false;
    }

    public String buildAns() {
        StringBuffer answer = new StringBuffer("YES\n");
        for (int i = 0; i < K; i++) {
            int mask = ans[i];
            boolean f = true;
            for (int j = 0; j < N; j++) {
                if ((mask & (1 << j)) != 0) {
                    answer.append(((f) ? "" : "+") + antiHash.get(input[j]));
                    f = false;
                }
            }
            answer.append("->" + antiHash.get(target[i]) + "\n");
        }
        return answer.toString();
    }

    public void solve() throws Exception {

        InputReader in = new InputReader();
        build();

        N = in.nextInt();
        K = in.nextInt();

        input = new int[N];
        for (int i = 0; i < N; i++) {
            input[i] = hash.get(in.next());
        }

        target = new int[K];
        for (int i = 0; i < K; i++) {
            target[i] = hash.get(in.next());
        }

        simpleMask = new int[1 << N];
        for (int i = 0; i < (1 << N); i++) {
            int currentMask = i;
            for (int from = 0; from < N; from++) {
                for (int to = 0; to <= from; to++) {
                    if (isOn(currentMask, from) && !isOn(currentMask, to)
                            && input[from] == input[to]) {
                        currentMask = turnOff(currentMask, from);
                        currentMask = turnOn(currentMask, to);
                    }
                }
            }
            simpleMask[i] = currentMask;
        }
        
        for (int i = 0; i < (1 << N); i++) {
            int sum = 0;
            for (int j = 0; j < N; j++)
                if ((i & (1 << j)) != 0) {
                    sum += input[j];
                }
            g[sum].add(i);
        }
        memo = new int[K + 4][(1 << N) + 10];
        for (int i = 0; i < memo.length; i++)
            Arrays.fill(memo[i], -1);
        ans = new int[K];
        boolean ret = go(0, 0);
        if (!ret) {
            System.out.println("NO");
            return;
        }
        System.out.print(buildAns());
    }

    public static void main(String[] args) throws Exception {
        new Round65_E().solve();
    }

    static class InputReader {
        BufferedReader in;
        StringTokenizer st;

        public InputReader() throws IOException {
            in = new BufferedReader(new InputStreamReader(System.in));
            st = new StringTokenizer(in.readLine());

        }

        public String next() throws IOException {

            while (!st.hasMoreElements())
                st = new StringTokenizer(in.readLine());
            return st.nextToken();
        }

        public int nextInt() throws NumberFormatException, IOException {
            return Integer.parseInt(next());
        }

        public long nextLong() throws NumberFormatException, IOException {
            return Long.parseLong(next());
        }
    }

    public void build() {
        g = new ArrayList[5000];
        for (int i = 0; i < g.length; i++) {
            g[i] = new ArrayList<Integer>();
        }
        hash = new HashMap<String, Integer>();
        hash.put("H", 1);
        hash.put("He", 2);
        hash.put("Li", 3);
        hash.put("Be", 4);
        hash.put("B", 5);
        hash.put("C", 6);
        hash.put("N", 7);
        hash.put("O", 8);
        hash.put("F", 9);
        hash.put("Ne", 10);
        hash.put("Na", 11);
        hash.put("Mg", 12);
        hash.put("Al", 13);
        hash.put("Si", 14);
        hash.put("P", 15);
        hash.put("S", 16);
        hash.put("Cl", 17);
        hash.put("Ar", 18);
        hash.put("K", 19);
        hash.put("Ca", 20);
        hash.put("Sc", 21);
        hash.put("Ti", 22);
        hash.put("V", 23);
        hash.put("Cr", 24);
        hash.put("Mn", 25);
        hash.put("Fe", 26);
        hash.put("Co", 27);
        hash.put("Ni", 28);
        hash.put("Cu", 29);
        hash.put("Zn", 30);
        hash.put("Ga", 31);
        hash.put("Ge", 32);
        hash.put("As", 33);
        hash.put("Se", 34);
        hash.put("Br", 35);
        hash.put("Kr", 36);
        hash.put("Rb", 37);
        hash.put("Sr", 38);
        hash.put("Y", 39);
        hash.put("Zr", 40);
        hash.put("Nb", 41);
        hash.put("Mo", 42);
        hash.put("Tc", 43);
        hash.put("Ru", 44);
        hash.put("Rh", 45);
        hash.put("Pd", 46);
        hash.put("Ag", 47);
        hash.put("Cd", 48);
        hash.put("In", 49);
        hash.put("Sn", 50);
        hash.put("Sb", 51);
        hash.put("Te", 52);
        hash.put("I", 53);
        hash.put("Xe", 54);
        hash.put("Cs", 55);
        hash.put("Ba", 56);
        hash.put("La", 57);
        hash.put("Hf", 72);
        hash.put("Ta", 73);
        hash.put("W", 74);
        hash.put("Re", 75);
        hash.put("Os", 76);
        hash.put("Ir", 77);
        hash.put("Pt", 78);
        hash.put("Au", 79);
        hash.put("Hg", 80);
        hash.put("Tl", 81);
        hash.put("Pb", 82);
        hash.put("Bi", 83);
        hash.put("Po", 84);
        hash.put("At", 85);
        hash.put("Rn", 86);
        hash.put("Fr", 87);
        hash.put("Ra", 88);
        hash.put("Ac", 89);
        hash.put("Rf", 104);
        hash.put("Db", 105);
        hash.put("Sg", 106);
        hash.put("Bh", 107);
        hash.put("Hs", 108);
        hash.put("Mt", 109);
        hash.put("Ds", 110);
        hash.put("Rg", 111);
        hash.put("Cn", 112);
        hash.put("Uuq", 114);
        hash.put("Uuh", 116);
        hash.put("Uuo", 118);
        hash.put("Ce", 58);
        hash.put("Pr", 59);
        hash.put("Nd", 60);
        hash.put("Pm", 61);
        hash.put("Sm", 62);
        hash.put("Eu", 63);
        hash.put("Gd", 64);
        hash.put("Tb", 65);
        hash.put("Dy", 66);
        hash.put("Ho", 67);
        hash.put("Er", 68);
        hash.put("Tm", 69);
        hash.put("Yb", 70);
        hash.put("Lu", 71);
        hash.put("Th", 90);
        hash.put("Pa", 91);
        hash.put("U", 92);
        hash.put("Np", 93);
        hash.put("Pu", 94);
        hash.put("Am", 95);
        hash.put("Cm", 96);
        hash.put("Bk", 97);
        hash.put("Cf", 98);
        hash.put("Es", 99);
        hash.put("Fm", 100);
        hash.put("Md", 101);
        hash.put("No", 102);
        hash.put("Lr", 103);
        antiHash = new HashMap<Integer, String>();
        for (Entry<String, Integer> e : hash.entrySet()) {
            antiHash.put(e.getValue(), e.getKey());
        }

    }

    private boolean isOn(int currentMask, int from) {
        return (currentMask & (1 << from)) != 0;
    }

    private int turnOff(int currentMask, int bit) {
        return currentMask & (~(1 << bit));
    }

    private int turnOn(int currentMask, int bit) {
        return currentMask | (1 << bit);
    }
}
