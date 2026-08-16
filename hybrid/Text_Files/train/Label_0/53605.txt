
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.Arrays;
import java.util.StringTokenizer;

public class TwoChandeliers {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String[] line1 = in.readLine().split(" ");

        int n = Integer.parseInt(line1[0]);
        int m = Integer.parseInt(line1[1]);
        long k = Long.parseLong(line1[2]);

        int[] color1 = readColorLine(in, n);
        int[] color2 = readColorLine(in, m);
        if (color1.length > color2.length) {
            int[] swap = color1;
            color1 = color2;
            color2 = swap;
        }

        int[] colorMap = buildColorMap(color1, color2);
        applyColorMap(color1, colorMap);
        applyColorMap(color2, colorMap);

        int[] numAngryDaysPerStart = numAngryDaysPerStart(color1.length, color2);
        //System.err.println(Arrays.toString(numAngryDaysPerStart));

        long numAngryFullLoop = numAngryFullLoop(numAngryDaysPerStart, color1.length);
        //System.err.println(numAngryFullLoop);

        long numFullLoops = k / numAngryFullLoop;
        if (numAngryFullLoop * numFullLoops == k) {
            numFullLoops -= 1;
        }
        BigInteger numDays = BigInteger.valueOf(numDaysFullLoop).multiply(BigInteger.valueOf(numFullLoops));
        k -= numAngryFullLoop * numFullLoops;

        int nextPos1 = 0;
        int nextPos2 = 0;
        long numDaysAdd = 0;
        while (k > 0) {
            if (nextPos1 == 0 && k > numAngryDaysPerStart[nextPos2]) {
                k -= numAngryDaysPerStart[nextPos2];
                nextPos2 += color1.length;
                numDaysAdd += color1.length;
            } else {
                if (color1[nextPos1] != color2[nextPos2]) {
                    k -= 1;
                }
                nextPos1 += 1;
                nextPos2 += 1;
                numDaysAdd += 1;
            }

            if (nextPos1 >= color1.length) nextPos1 -= color1.length;
            if (nextPos2 >= color2.length) nextPos2 -= color2.length;
        }
        System.out.println(numDays.add(BigInteger.valueOf(numDaysAdd)));
    }

    static int[] readColorLine(BufferedReader in, int len) throws IOException {
        StringTokenizer line = new StringTokenizer(in.readLine());
        int[] res = new int[len];
        for (int i = 0; i < len; ++i) {
            res[i] = Integer.parseInt(line.nextToken()) - 1;
        }
        return res;
    }
    static int[] buildColorMap(int[] color1, int[] color2) {
        int[] colorMap = new int[2*Math.max(color1.length,color2.length)];
        Arrays.fill(colorMap, -1);
        for (int i = 0; i < color1.length; ++i) {
            colorMap[color1[i]] = i;
        }
        return colorMap;
    }
    static void applyColorMap(int[] color, int[] map) {
        for (int i = 0; i < color.length; ++i) {
            color[i] = map[color[i]];
        }
    }
    static int[] numAngryDaysPerStart(int jumpLen, int[] color2) {
        int[] startPos = new int[color2.length];
        for (int i = 0; i < color2.length; ++i) {
            if (color2[i] == -1) continue;
            int matchStartPos = i - color2[i];
            while (matchStartPos < 0) matchStartPos += color2.length;
            startPos[matchStartPos] += 1;
        }
        for (int i = 0; i < startPos.length; ++i) {
            startPos[i] = jumpLen - startPos[i];
        }
        return startPos;
    }
    static long numDaysFullLoop = 0;
    static long numAngryFullLoop(int[] numAngryPerStart, int jump) {
        long result = 0;
        int i = 0;
        do {
            result += numAngryPerStart[i];

            i += jump;
            numDaysFullLoop += jump;
            if (numAngryPerStart.length <= i) i -= numAngryPerStart.length;
        } while (i != 0);
        return result;
    }
}
