import java.io.*;
import java.math.BigInteger;
import java.util.BitSet;

/**
 * Created by simin on 3/4/15.
 */
public class D
{
    public static final int max = 2000 + 7;
    public static void main(String [] strings) throws IOException
    {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int m = Integer.parseInt(reader.readLine());
        BitSet []bitSet = new BitSet[m];
        BitSet []affect = new BitSet[m];
        for (int i = 0; i < m; i++)
        {
            BigInteger bigInteger = new BigInteger(reader.readLine());
            bitSet[i] = new BitSet(max);
            affect[i] = new BitSet(m);
            affect[i].set(i, true);
            for (int j = 0; j < max; j++)
            {
                bitSet[i].set(j, bigInteger.testBit(j));
            }
        }
        PrintWriter writer = new PrintWriter(new OutputStreamWriter(System.out));
        int column = 0;
        for (int i = 0; i < m; i++)
        {
            int j = column;
            while (j < max && !bitSet[i].get(j))
                j++;
            if (j == max)
            {
                writer.print(affect[i].cardinality() - 1);
                for (int k = 0; k < m; k++)
                    if (affect[i].get(k) && i != k)
                        writer.print(" " + k);
                writer.println();
                continue;
            }
            for (int k = 0; k < m; k++)
            {
                boolean tmp = bitSet[k].get(column);
                bitSet[k].set(column, bitSet[k].get(j));
                bitSet[k].set(j, tmp);
            }
            for (int k = i + 1; k < m; k++)
                if (bitSet[k].get(column))
                {
                    affect[k].xor(affect[i]);
                    bitSet[k].xor(bitSet[i]);
                }
            writer.println(0);
            column++;
        }

        writer.flush();
        writer.close();
    }
}
