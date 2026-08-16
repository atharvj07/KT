import java.awt.Point;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.StringTokenizer;

public class H {

    BufferedReader in;
    PrintWriter out;
    StringTokenizer tok;

    void init() {
        try {
            in = new BufferedReader(new FileReader("input.txt"));
            out = new PrintWriter("output.txt");
        } catch (Exception e) {
            in = new BufferedReader(new InputStreamReader(System.in));
            out = new PrintWriter(System.out);
        }
    }

    String readString() {
        try {
            while (tok == null || !tok.hasMoreTokens()) {
                tok = new StringTokenizer(in.readLine());
            }
            return tok.nextToken();
        } catch (Exception e) {
            return null;
        }
    }

    int readInt() {
        return Integer.parseInt(readString());
    }

    long readLong() {
        return Long.parseLong(readString());
    }

    int[] readIntArray(int n) {
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = readInt();
        }
        return a;
    }

    public static void main(String[] args) {
        new H().run();
    }

    void run() {
        try {
            long tStart = System.currentTimeMillis();
            init();
            solve();
            in.close();
            out.close();
            long tEnd = System.currentTimeMillis();

            System.err.println(tEnd - tStart);
        } catch (Exception e) {
            e.printStackTrace();
            System.exit(-1);
        }
    }

    void solve() {
        int trainersCount = readInt();
        int edgesCount = readInt();

        Point[] edges = new Point[edgesCount];
        for (int i = 0; i < edgesCount; ++i) {
            int from = readInt() - 1;
            int to = readInt() - 1;
            edges[i] = new Point(from, to);
        }

        List<Integer>[] trainersTeams = new List[trainersCount];
        int teamsCount = 0;

        for (int i = 0; i < trainersCount; ++i){
            int size = readInt();
            List<Integer> trainerTeams = new ArrayList<>(size);

            for (int j = 0; j < size; ++j) {
                int team = readInt() - 1;
                teamsCount = Math.max(teamsCount, team + 1);

                trainerTeams.add(team);
            }

            trainersTeams[i] = trainerTeams;
        }

        Random rnd = new Random();

        int[] mappedTeams = new int[trainersCount];
        boolean[] isEnemyConferences = new boolean[teamsCount];

        while (true) {
            for (int trainer = 0; trainer < trainersCount; ++trainer) {
                List<Integer> trainerTeams = trainersTeams[trainer];
                int trainerTeamIndex = rnd.nextInt(trainerTeams.size());
                mappedTeams[trainer] = trainerTeams.get(trainerTeamIndex);
            }

            for (int team = 0; team < teamsCount; ++team) {
                isEnemyConferences[team] = rnd.nextBoolean();
            }

            int enemyEdgesCount = 0;
            for (Point edge : edges) {
                int fromTeam = mappedTeams[edge.x];
                int toTeam = mappedTeams[edge.y];
                if (isEnemyConferences[fromTeam] != isEnemyConferences[toTeam]) {
                    ++enemyEdgesCount;
                }
            }

            if (enemyEdgesCount * 2 >= edgesCount) {
                break;
            }
        }

        for (int mappedTeam : mappedTeams) {
            out.print((mappedTeam + 1) + " ");
        }
        out.println();

        for (boolean isEnemyConference : isEnemyConferences) {
            int conference = (isEnemyConference ? 1 : 2);
            out.print(conference + " ");
        }
        out.println();
    }
}
