import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {

    /** 座席数 */
    private final static int SEATS = 17;

    /** 客グループ数 */
    private final static int GROUP = 100;

    /** 客グループの到着する間隔（分） */
    private final static int INTERVAL = 5;

    /** 客グループの待ち時間を格納する配列 */
    private static int[] watingTimes = new int[GROUP];

    /** 客グループの到着時刻、人数、食事時間を格納する二次元配列 */
    private static int[][] groupInfo = new int[GROUP][3];

    /** 客グループの到着時刻を表す添え字 */
    private final static int GROUP_INFO_ARRIVAL = 0;

    /** 客グループの人数を表す添え字 */
    private final static int GROUP_INFO_PERSONS = 1;

    /** 客グループの食事時間を表す添え字 */
    private final static int GROUP_INFO_EATING_MINUTES = 2;

    /** 座席の着席状況を格納する配列 */
    private static int[] seatsCondition = new int[SEATS];

    /** お店が開いているかどうか */
    private static boolean openFlag = true;

    /** 最後に到着したグループ */
    private static int lastArrivalGroup = -1;

    /** 待ちグループ数 */
    private static int watingGroups = 0;

    /** 正午からの経過時間（分） */
    private static int passedMinutes = 0;

    /**
     * <p>
     * 「福縞軒」に訪れる客グループの待ち時間を算出する。
     * </p>
     *
     * @param args
     *            利用しない。
     * @throws IOException
     * @throws NumberFormatException
     */
    public static void main(String[] args) throws NumberFormatException,
            IOException {

        // 入力値の読み込み
        List<Integer> inputList = getInput();

        // 全客グループの到着時間と人数と食事時間を求める
        setGroupInfo();

        while (openFlag) {

            // 等間隔で次のグループが到着する
            if (passedMinutes % INTERVAL == 0) {
                lastArrivalGroup++;
                watingGroups++;
            }

            // 待ちグループがいなければ何もせずに時刻を進める
            if (watingGroups == 0) {
                passedMinutes++;
                continue;
            }

            // 待ちグループが存在した場合
            // 待ちの先頭グループ番号を求める
            int nextGroup = lastArrivalGroup - watingGroups + 1;

            // 待ちグループがいて、空席が存在する場合　※最初の１回は必ず空席チェックする
            boolean vacancyFlag = true; // 空席が存在するかのフラグ
            while (watingGroups != 0 && vacancyFlag) {

                // 待ちの先頭グループの人数を求める
                int numberOfPersons = groupInfo[nextGroup][GROUP_INFO_PERSONS];

                // 退席時刻となった席を空席にし、先頭のグループが着席できる座席の番号を求める
                int seatNumber = getSeatNumber(numberOfPersons);

                if (seatNumber != -1) {

                    // 着席できる座席があった場合、座席にグループの退席時刻を設定する
                    for (int i = 0; i < numberOfPersons; i++) {
                        seatsCondition[seatNumber] = passedMinutes
                                + groupInfo[nextGroup][GROUP_INFO_EATING_MINUTES];
                        seatNumber++;
                    }

                    // グループの待ち時間を設定する
                    watingTimes[nextGroup] = passedMinutes
                            - groupInfo[nextGroup][GROUP_INFO_ARRIVAL];

                    // 待ちグループ数を減らす
                    watingGroups--;
                    nextGroup = lastArrivalGroup - watingGroups + 1;

                    // 最後のグループが座ったら、お店を閉店する
                    if (nextGroup == GROUP) {
                        openFlag = false;
                        vacancyFlag = false;
                    }
                } else {
                    vacancyFlag = false;
                }
            }

            passedMinutes++;
        }

        // 結果を出力する
        for (int i : inputList) {
            System.out.println(watingTimes[i]);
        }
    }

    /**
     * <p>
     * 入力値（n番目のグループ）を取得する
     * </p>
     *
     * @return 入力値のリスト
     * @throws NumberFormatException
     * @throws IOException
     */
    private static List<Integer> getInput() throws NumberFormatException,
            IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        List<Integer> inputList = new ArrayList<Integer>();

        String line = null;
        while ((line = br.readLine()) != null) {
            inputList.add(Integer.parseInt(line));
        }

        return inputList;
    }

    /**
     * <p>
     * 客グループの到着時刻、人数、食事時間を計算し、配列にセットする
     * </p>
     */
    private static void setGroupInfo() {

        for (int i = 0; i < GROUP; i++) {
            groupInfo[i][GROUP_INFO_ARRIVAL] = i * INTERVAL;
            groupInfo[i][GROUP_INFO_PERSONS] = (i % 5 == 1 ? 5 : 2);
            groupInfo[i][GROUP_INFO_EATING_MINUTES] = 17 * (i % 2) + 3
                    * (i % 3) + 19;
        }

    }

    /**
     * <p>
     * 退席時刻となった席を空席にする。<br/>
     * 引数で受け取った人数が座れる席を探し、座席番号を返す。<br/>
     * 座席がない場合は-1を返す。
     * </p>
     *
     * @param numberOfPersons
     *            人数
     * @return 座席番号
     */
    private static int getSeatNumber(int numberOfPersons) {

        int seatNumber = 0; // 先頭の座席番号
        int vacancySeats = 0; // 空席数

        for (int i = 0; i < SEATS; i++) {

            // 退席時刻となった座席を空席に戻す
            if (seatsCondition[i] <= passedMinutes) {
                seatsCondition[i] = 0;
            }

            if (seatsCondition[i] == 0) {

                // 席が空席であれば、空席数を増やす
                vacancySeats++;

                // 空席数が待ち人数と等しければ、先頭の座席番号を返す
                if (vacancySeats == numberOfPersons) {
                    return seatNumber;
                }
            } else {

                // 席が空席でなければ、座席番号を次に移し、空席数を0に戻す
                seatNumber = i + 1;
                vacancySeats = 0;
            }
        }

        // 空席がなければ-1を返す
        return -1;
    }
}