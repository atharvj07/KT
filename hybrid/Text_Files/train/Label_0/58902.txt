import java.io.*;
import java.util.*;

public class D {
    public static void main(String[] args) throws IOException {
        new D().solve();
    }

    static final boolean DEBUG = System.getProperty("ONLINE_JUDGE") == null;
    Card J1 = new Card("J", "1");
    Card J2 = new Card("J", "2");

    BufferedReader br;
    StringTokenizer st = new StringTokenizer("");

    void solve() throws IOException {
        br = new BufferedReader(new InputStreamReader(DEBUG ? new FileInputStream("input.txt") :System.in));
        int n = nextInt();
        int m = nextInt();
        Set<Card> all = createAllCards();
        Card[][] cards = new Card[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                String token = nextToken();
                cards[i][j] = new Card(token.substring(0, 1), token.substring(1, 2));
            }
        }
        br.close();

        Set<Card> restCards = new HashSet<Card>(all);
        for (Card[] row : cards) {
            for (Card card : row) {
                restCards.remove(card);
            }
        }

        Map<Card, Card> ans = new HashMap<Card, Card>();
        Card[] jokers = new Card[] {J1, J2};
        Info can = find(restCards, cards, jokers, 0, ans);
        PrintWriter pw = new PrintWriter(System.out);
        if (can != null) {
            pw.println("Solution exists.");
            if (ans.isEmpty()) {
                pw.println("There are no jokers.");
            } else {
                String delim = "";
                String str = "Replace ";
                for (Card joker : jokers) {
                    Card to = ans.get(joker);
                    if (to != null) {
                        str += delim;
                        str += joker.toString() + " with " + to.toString();
                        delim = " and ";
                    }
                }
                str += ".";
                pw.println(str);
            }
            pw.println("Put the first square to (" + can.i1 + ", " + can.j1 + ").");
            pw.println("Put the second square to (" + can.i2 + ", " + can.j2 + ").");
        } else {
            pw.println("No solution.");
        }
        pw.close();
    }

    Info find(Set<Card> restCards, Card[][] cards, Card[] jokers, int jokerInd, Map<Card, Card> ans) {
        if (jokerInd == jokers.length) {
            return check(cards);
        }
        int ic = -1, jc = -1;
        final int n = cards.length, m = cards[0].length;
        Card joker = jokers[jokerInd];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (cards[i][j].equals(joker)) {
                    ic = i;
                    jc = j;
                    break;
                }
            }
        }
        if (ic == -1) {
            return find(restCards, cards, jokers, jokerInd + 1, ans);
        }
        for (Card newCard : restCards) {
            cards[ic][jc] = newCard;
            Set<Card> newRest = new HashSet<Card>(restCards);
            newRest.remove(newCard);
            Info info = find(newRest, cards, jokers, jokerInd + 1, ans);
            cards[ic][jc] = joker;
            if (info != null) {
                ans.put(joker, newCard);
                return info;
            }
        }
        return null;
    }

    Info check(Card[][] cards) {
        final int n = cards.length;
        int m = cards[0].length;
        for (int i1 = 0; i1 <= n - 3; i1++) {
            for (int j1 = 0; j1 <= m - 3; j1++) {
                if (!validate(cards, i1, j1)) {
                    continue;
                }
                for (int i2 = i1; i2 <= n - 3; i2++) {
                    for (int j2 = 0; j2 <= m - 3; j2++) {
                        if (!intersect(i1, j1, i2, j2)) {
                            if (validate(cards, i2, j2)) {
                                return new Info(i1, j1, i2, j2);
                            }
                        }
                    }
                }
            }
        }
        return null;
    }

    boolean intersect(int i1, int j1, int i2, int j2) {
        return inside(i1, j1, i2,     j2) ||
               inside(i1, j1, i2 + 2, j2) ||
               inside(i1, j1, i2,     j2 + 2) ||
               inside(i1, j1, i2 + 2, j2 + 2);
    }

    boolean inside(int i0, int j0, int i, int j) {
        return i0 <= i && i < i0 + 3 && j0 <= j && j < j0 + 3;
    }

    boolean validate(Card[][] cards, int i0, int j0) {
        Set<String> suites = new HashSet<String>();
        Set<String> values = new HashSet<String>();
        for (int i = i0; i < i0 + 3; i++) {
            for (int j = j0; j < j0 + 3; j++) {
                suites.add(cards[i][j].suit);
                values.add(cards[i][j].value);
            }
        }
        return suites.size() == 1 || values.size() == 9;
    }

    private Set<Card> createAllCards() {
        Set<Card> all = new HashSet<Card>();
        String[] values = new String[] {"2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"};
        String[] suits = new String[] {"C", "D", "H", "S"};
        for (String value : values) {
            for (String suit : suits) {
                all.add(new Card(value, suit));
            }
        }
        return all;
    }

    String nextToken() throws IOException {
        while (!st.hasMoreTokens()) {
            st = new StringTokenizer(br.readLine());
        }
        return st.nextToken();
    }

    int nextInt() throws IOException {
        return Integer.parseInt(nextToken());
    }

    static class Card {
        final String value;
        final String suit;

        Card(String value, String suit) {
            this.value = value;
            this.suit = suit;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;

            Card card = (Card) o;

            return suit.equals(card.suit) && value.equals(card.value);
        }

        @Override
        public int hashCode() {
            int result = value != null ? value.hashCode() : 0;
            result = 31 * result + (suit != null ? suit.hashCode() : 0);
            return result;
        }

        @Override
        public String toString() {
            return value + suit;
        }
    }

    static class Info {
        final int i1, j1;
        final int i2, j2;

        Info(int i1, int j1, int i2, int j2) {
            this.i1 = i1 + 1;
            this.j1 = j1 + 1;
            this.i2 = i2 + 1;
            this.j2 = j2 + 1;
        }
    }
}
