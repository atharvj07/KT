import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

import static java.lang.Integer.parseInt;

/**
 * Related Products
 */
public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String line;
		String[] words;

		line = br.readLine();

		int N, F;
		N = parseInt(line.substring(0, line.indexOf(' ')));
		F = parseInt(line.substring(line.indexOf(' ') + 1));

		Map<String, Integer> itemsByName = new TreeMap<>();
		Map<Integer, String> itemsById = new TreeMap<>();
		List<String[]> infos = new ArrayList<>();

		for (int i = 0; i < N; i++) {
			words = br.readLine().split(" ");
			for (int j = 1; j < words.length; j++) {
				itemsByName.putIfAbsent(words[j], 0);
			}
			Arrays.sort(words);
			infos.add(words);
		}

		{
			int i = 0;
			for (String item : itemsByName.keySet()) {
				itemsByName.replace(item, i);
				itemsById.put(i, item);
				i++;
			}
		}

		int[][] rels = new int[itemsByName.size()][itemsByName.size()];

		for (String[] info : infos) {
			for (int i = 1; i < info.length; i++) {
				for (int j = i + 1; j < info.length; j++) {
					int _i, _j;
					_i = itemsByName.get(info[i]);
					_j = itemsByName.get(info[j]);
					rels[_i][_j]++;
				}
			}
		}

		//solve
		List<String> results = new ArrayList<>();

		for (int i = 0; i < rels.length; i++) {
			for (int j = 0; j < rels.length; j++) {
				if (rels[i][j] >= F) {
					results.add(itemsById.get(i) + " " + itemsById.get(j));
				}
			}
		}

		System.out.println(results.size());

		if (results.size() != 0) {
			for (String result : results) {
				System.out.println(result);
			}
		}

	} // end main
}