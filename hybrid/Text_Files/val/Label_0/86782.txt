import java.io.BufferedInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;

public class Main {

    private final static InputReader inputReader = new InputReader(System.in);
    private final static OutputWriter outputWriter = new OutputWriter(System.out);

    public static void main(String[] args) throws IOException {
        int numberOfTestCases = 1;//inputReader.scanInt();
        for (int testCase = 1; testCase <= numberOfTestCases; ++testCase) {
            final ProblemParameters parameters = new ProblemParameters();
            parameters.number = inputReader.scanString();
            parameters.requiredDivisibility = inputReader.scanInt();

            final Solver solver = new Solver(parameters);
            solver.solve();
        }

        outputWriter.close();
    }

    static class Solver {

        private final static long MOD = 1000000007;
        private final ProblemParameters parameters;
        private final long[][] dp;

        public Solver(final ProblemParameters parameters) {
            this.parameters = parameters;
            this.dp = new long[parameters.number.length() + 1][parameters.requiredDivisibility];
            resetDpStates();
        }

        private void resetDpStates() {
            for (int digitPos = 0; digitPos <= parameters.number.length(); ++digitPos) {
                for (int digitSum = 0; digitSum < parameters.requiredDivisibility; ++digitSum) {
                    dp[digitPos][digitSum] = -1;
                }
            }
        }

        public void solve() {
            final long answer = digitDp();
            outputWriter.println(answer);
        }

        private long digitDp() {
            final int lengthOfNumber = parameters.number.length();
            int rem = lengthOfNumber - 1;
            int digitSum = 0;
            long answer = -1;
            for (int currentPosOfDigit = 0; currentPosOfDigit < lengthOfNumber; ++currentPosOfDigit) {
                int currentDigit = parameters.number.charAt(currentPosOfDigit) - '0';
                for (int nextDigit = 0; nextDigit < currentDigit; ++nextDigit) {
                    final int newDigitSum = getUpdatedDigitSum (digitSum, nextDigit);
                    answer += rec(rem - 1, newDigitSum);
                    answer = updateWithMOD(answer);
                }
                digitSum = getUpdatedDigitSum(digitSum, currentDigit);
                rem--;
            }

            if (digitSum == 0) {
                answer++;
                answer = updateWithMOD(answer);
            }

            return answer;
        }

        private long rec(final int remPos, final int digitSum) {
            if (remPos < 0) {
                return digitSum == 0 ? 1 : 0;
            }

            if (dp[remPos][digitSum] != -1) {
                return dp[remPos][digitSum];
            }

            long answer = 0;
            for (int currentDigit = 0; currentDigit <= 9; ++currentDigit) {
                final int newDigitSum = getUpdatedDigitSum(digitSum, currentDigit);
                answer += rec(remPos - 1, newDigitSum);
                answer = updateWithMOD(answer);
            }
            dp[remPos][digitSum] = answer;

            return answer;
        }

        private int getUpdatedDigitSum(final int currentDigitSum, final int currentDigit) {
            return (currentDigitSum + currentDigit) % parameters.requiredDivisibility;
        }

        private long updateWithMOD(final long val) {
            long newVal = val;
            if (newVal < 0) {
                newVal += MOD;
            }

            if (newVal >= MOD) {
                newVal %= MOD;
            }

            return newVal;
        }
    }

    static class ProblemParameters {

        String number;
        int requiredDivisibility;
    }

    static class Pair<F, S> {

        F first;
        S second;

        public Pair(final F first, final S second) {
            this.first = first;
            this.second = second;
        }
    }

    static class MatrixLib {

        private final long modulo;

        private MatrixLib(final long mod) {
            this.modulo = mod;
        }

        public Matrix pow(final Matrix matrix, long exponent) {
            Matrix resultantMatrix = Matrix.getIdentityMatrix(matrix.rowSize, matrix.colSize);
            Matrix copyOfSourceMatrix = new Matrix(matrix.rowSize, matrix.colSize);
            copyOfSourceMatrix.copyFrom(matrix);

            while (exponent > 0) {
                if ((exponent & 1) != 0) {
                    resultantMatrix = multiply(resultantMatrix, copyOfSourceMatrix);
                }

                exponent >>= 1;
                copyOfSourceMatrix = multiply(copyOfSourceMatrix, copyOfSourceMatrix);
            }

            return resultantMatrix;
        }

        private Matrix multiply(final Matrix firstMatrix, final Matrix secondMatrix) {
            assert firstMatrix.colSize == secondMatrix.rowSize;
            final Matrix resultantMatrix = new Matrix(firstMatrix.rowSize, secondMatrix.colSize);
            for (int row = 0; row < firstMatrix.rowSize; ++row) {
                for (int col = 0; col < secondMatrix.colSize; ++col) {
                    for (int inter = 0; inter < secondMatrix.rowSize; ++inter) {
                        long currentValue = resultantMatrix.getValueAt(row, col);
                        long multiplyValue = firstMatrix.getValueAt(row, inter) * secondMatrix.getValueAt(inter, col);
                        long updatedValue = adjustWithMod(adjustWithMod(currentValue) + adjustWithMod(multiplyValue));
                        resultantMatrix.setValueAt(row, col, updatedValue);
                    }
                }
            }

            return resultantMatrix;
        }

        private long adjustWithMod(final long value) {
            return value >= modulo
                    ? value % modulo
                    : (value < 0)
                    ? (value + modulo) % modulo
                    : value;
        }
    }

    static class Matrix {

        int rowSize;
        int colSize;
        long[][] matrix;

        public Matrix(final int rowSize, final int colSize) {
            this.rowSize = rowSize;
            this.colSize = colSize;
            this.matrix = new long[rowSize + 1][colSize + 1];
        }

        public void setValueAt(final int row, final int col, final long value) {
            this.matrix[row][col] = value;
        }

        public long getValueAt(final int row, final int col) {
            return this.matrix[row][col];
        }

        public void copyFrom(final Matrix sourceMatrix) {
            assert sourceMatrix.rowSize == rowSize && sourceMatrix.colSize == colSize;
            for (int row = 0; row < rowSize; ++row) {
                for (int col = 0; col < colSize; ++col) {
                    setValueAt(row, col, sourceMatrix.getValueAt(row, col));
                }
            }
        }

        public static Matrix getIdentityMatrix(final int rows, final int cols) {
            assert rows == cols : "Asked matrix is not square matrix can not provide identity matrix.";
            final Matrix resultantMatrix = new Matrix(rows, cols);
            for (int row = 0; row < rows; ++row) {
                resultantMatrix.setValueAt(row, row, 1);
            }

            return resultantMatrix;
        }

        @Override
        public String toString() {
            StringBuffer stringBuffer = new StringBuffer();
            stringBuffer.append("rowSize -> " + rowSize + " colSize -> " + colSize + "\n");
            for (int i = 0; i < rowSize; ++i) {
                for (int j = 0; j < colSize; ++j) {
                    stringBuffer.append(matrix[i][j] + " ");
                }
                stringBuffer.append("\n");
            }

            return stringBuffer.toString();
        }
    }

    static class NumberTheoryLib {

        public List<Integer> getMobiousFunctionValuesTill(final int maximumValue) {
            final List<Integer> mobiousFunctionValues = new ArrayList<>();
            mobiousFunctionValues.add(0); // For 0 dummy value
            mobiousFunctionValues.add(1); // For 1

            final int[] lowestPrimeDivisor = new int[maximumValue + 2];
            for (int currentNumber = 2; currentNumber <= maximumValue; ++currentNumber) {
                if (lowestPrimeDivisor[currentNumber] == 0) {
                    for (int multipleOfCurrentNumber = currentNumber; multipleOfCurrentNumber <= maximumValue;
                         multipleOfCurrentNumber += currentNumber) {
                        lowestPrimeDivisor[multipleOfCurrentNumber] = currentNumber;
                    }
                }

                boolean isNumberSqureFree = true;
                int numberOfDistinctPrimeDivisors = 0;
                int tempValueOfCurrentNumber = currentNumber;
                while (tempValueOfCurrentNumber > 1) {
                    int divisor = lowestPrimeDivisor[tempValueOfCurrentNumber];
                    if (tempValueOfCurrentNumber % divisor == 0) {
                        tempValueOfCurrentNumber /= divisor;
                        if (tempValueOfCurrentNumber % divisor == 0) { // Not a squareFree
                            isNumberSqureFree = false;
                            break;
                        }

                        numberOfDistinctPrimeDivisors++;
                    }
                }

                if (isNumberSqureFree) {
                    mobiousFunctionValues.add((numberOfDistinctPrimeDivisors & 1) != 0 ? -1 : 1);
                } else {
                    mobiousFunctionValues.add(0);
                }
            }

            return mobiousFunctionValues;
        }
    }

    static class SegmentTree { // Assuming segment will start from 0

        private long[] tree;
        private int expectedNumberOfElements;
        private SegmentTreeProperty property;

        public SegmentTree(final int expectedNumberOfElements, final SegmentTreeProperty property) {
            this.expectedNumberOfElements = expectedNumberOfElements;
            this.tree = new long[4 * expectedNumberOfElements];
            this.property = property;
        }

        public void updateForOnePoint(final int index, final long valueToUpdate) {
            update(1, 0, expectedNumberOfElements - 1, index, index, valueToUpdate);
        }

        private void update(final int treeNode, final int start, final int end, final int updateStart,
                            final int updateEnd, final long value) {
            if (updateStart <= start && updateEnd >= end) {
                final long existingValue = tree[treeNode];
                final long updatedValue = property.combine(existingValue, value);
                tree[treeNode] = updatedValue;
                return;
            }

            if (start > end || start > updateEnd || end < updateStart) {
                return;
            }

            final int leftNode = getLeftNodeFor(treeNode);
            final int endOfLeftNode = getEndForLeftNode(start, end);
            update(leftNode, start, endOfLeftNode, updateStart, updateEnd, value);

            final int rightNode = getRightNodeFor(treeNode);
            final int startOfRightNode = getStartOfRightNode(start, end);
            update(rightNode, startOfRightNode, end, updateStart, updateEnd, value);

            final long leftTreeValue = tree[leftNode];
            final long rightTreeValue = tree[rightNode];
            final long combinedResultOfSubTrees = property.combine(leftTreeValue, rightTreeValue);
            tree[treeNode] = combinedResultOfSubTrees;
        }

        public long query(final int startInSegment, final int endInSegment) {
            return query(1, 0, expectedNumberOfElements - 1, startInSegment, endInSegment);
        }

        private long query(final int treeNode, final int start, final int end, final int queryStart,
                           final int queryEnd) { // This is not accepted signature, but in CP world we don't care about best practices. :P
            if (queryStart <= start && queryEnd >= end) {
                return tree[treeNode];
            }

            if (start > end || start > queryEnd || end < queryStart) {
                return property.getValueForOutOfBound();
            }

            final int leftNode = getLeftNodeFor(treeNode);
            final int endOfLeftNode = getEndForLeftNode(start, end);
            final long leftPartOfTree = query(leftNode, start, endOfLeftNode, queryStart, queryEnd);

            final int rightNode = getRightNodeFor(treeNode);
            final int startOfRightNode = getStartOfRightNode(start, end);
            final long rightPartOfTree = query(rightNode, startOfRightNode, end, queryStart, queryEnd);

            return property.combine(leftPartOfTree, rightPartOfTree);
        }

        private int getLeftNodeFor(final int currentNode) {
            return (currentNode << 1);
        }

        private int getRightNodeFor(final int currentNode) {
            return getLeftNodeFor(currentNode) + 1;
        }

        private int getEndForLeftNode(final int start, final int end) {
            return (start + end) >> 1;
        }

        private int getStartOfRightNode(final int start, final int end) {
            return getEndForLeftNode(start, end) + 1;
        }
    }

    interface SegmentTreeProperty {

        long getValueForOutOfBound();

        long combine(final long leftPart, final long rightPart);
    }

    static class MaxSegmentTreeProperty implements SegmentTreeProperty {

        public long getValueForOutOfBound() {
            return 0L;
        }

        public long combine(final long leftPart, final long rightPart) {
            return Math.max(leftPart, rightPart);
        }
    }

    // We can use abstract method or loaner pattern to create different classes for different dataTypes and
    // keep repeated code in with generic class. But can't follow OOPS in CP :( because of TLE or MLE.
    // So try to use less object creation in CP.
    static class InputReader {

        private final BufferedInputStream bufferedInputStream;

        private final static char NEGATIVE_CHAR = '-';
        private final static char SPACE_CHAR = ' ';
        private final static char TAB_CHAR = '\t';
        private final static char NEW_LINE_WITH_N = '\n';
        private final static char NEW_LINE_WITH_R = '\r';
        private final static int END_OF_INPUT_STREAM = -1;

        public InputReader(final InputStream inputStream) {
            bufferedInputStream = new BufferedInputStream(inputStream);
        }

        public int scanInt() throws IOException {
            int currentByte = findFirstUsefulByte();
            boolean isNegative = false;
            if (currentByte == NEGATIVE_CHAR) {
                isNegative = true;
                currentByte = bufferedInputStream.read();
            }

            int number = 0;
            while (isUsefulByte(currentByte)) {
                number = (number * 10) + (currentByte - '0');
                currentByte = bufferedInputStream.read();
            }

            return isNegative ? -number : number;
        }

        public long scanLong() throws IOException {
            int currentByte = findFirstUsefulByte();
            boolean isNegative = false;
            if (currentByte == NEGATIVE_CHAR) {
                isNegative = true;
                currentByte = bufferedInputStream.read();
            }

            long number = 0;
            while (isUsefulByte(currentByte)) {
                number = (number * 10) + (currentByte - '0');
                currentByte = bufferedInputStream.read();
            }

            return isNegative ? -number : number;
        }

        public String scanString() throws IOException {
            int currentByte = findFirstUsefulByte();
            final StringBuilder stringBuilder = new StringBuilder();
            while (isUsefulByte(currentByte)) {
                stringBuilder.append((char) currentByte);
                currentByte = bufferedInputStream.read();
            }

            return stringBuilder.toString();
        }

        public double scanDouble() throws IOException { //Reason to use java's parser is because we had to write a lot of cases to handle floating point problems.
            return Double.parseDouble(scanString());
        }

        public List<Integer> scanListOfIntegers(int numbersCount) throws IOException {
            final List<Integer> numberList = new ArrayList<>();
            while (numbersCount-- > 0) {
                numberList.add(scanInt());
            }

            return numberList;
        }

        public List<Long> scanListOfLongs(int numbersCount) throws IOException {
            final List<Long> numberList = new ArrayList<>();
            while (numbersCount-- > 0) {
                numberList.add(scanLong());
            }

            return numberList;
        }

        public List<String> scanListOfStrings(int numbersCount) throws IOException {
            final List<String> stringList = new ArrayList<>();
            while (numbersCount-- > 0) {
                stringList.add(scanString());
            }

            return stringList;
        }

        public List<Double> scanListOfDoubles(int numbersCount) throws IOException {
            final List<Double> doubleList = new ArrayList<>();
            while (numbersCount-- > 0) {
                doubleList.add(scanDouble());
            }

            return doubleList;
        }

        private int findFirstUsefulByte() throws IOException {
            int currentByte = bufferedInputStream.read();
            while (!isUsefulByte(currentByte)) {
                currentByte = bufferedInputStream.read();
            }

            return currentByte;
        }

        private boolean isUsefulByte(final int currentByte) {
            if (currentByte == SPACE_CHAR || NEW_LINE_WITH_N == currentByte || NEW_LINE_WITH_R == currentByte
                    || currentByte == TAB_CHAR || currentByte == END_OF_INPUT_STREAM) {
                return false;
            } else {
                return true;
            }
        }
    }

    // Try to use it in tr-resource block.
    // To avoid close call manually.
    static class OutputWriter implements AutoCloseable {

        private final static boolean IS_AUTO_FLUSH_FOR_NEW_LINE = true;
        private final PrintWriter printWriter;

        public OutputWriter(final OutputStream outputStream) {
            this.printWriter = new PrintWriter(outputStream, IS_AUTO_FLUSH_FOR_NEW_LINE);
        }

        public void print(Object... objects) {
            for (int objectIndex = 0; objectIndex < objects.length; ++objectIndex) {
                if (objectIndex != 0) {
                    printWriter.print(' ');
                }
                printWriter.print(objects[objectIndex]);
            }
        }

        public void println(Object... objects) {
            print(objects);
            printWriter.println();
        }

        public void flush() { //Force flush if require after printing each element on one line
            printWriter.flush();
        }

        public void close() {
            printWriter.close();
        }
    }
}