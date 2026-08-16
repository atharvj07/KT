import java.io.*;
import java.util.*;

public class minFolder
{
	public static void main(String[] args) throws IOException
	{
		PrintWriter writer = new PrintWriter(new OutputStreamWriter(System.out));
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

		int n = Integer.parseInt(reader.readLine().trim());

		int cnt = 0, res = 0;
		ArrayList<Integer> folder = new ArrayList<Integer>();

		StringTokenizer st = new StringTokenizer(reader.readLine());

		for(int i = 0; i < n; i++)
		{
			res++;
			int num = Integer.parseInt(st.nextToken());

			if(num < 0)
				cnt++;

			if(cnt == 3)
			{
				folder.add(res-1);
				res = cnt = 1;
			}
		}
		if(res != 0)
			folder.add(res);

		writer.println(folder.size() == 0 ? 1 : folder.size());

		for(int i = 0; i < folder.size(); i++)
			writer.print(folder.get(i) + (i != folder.size()-1 ? " ": "\n"));

		writer.flush();
		writer.close();

	}
}
