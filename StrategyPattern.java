class CodeThatUsesSomeAlgorithm {
    private Algorithm algorithmInstance;

    public void setAlgorithm(Algorithm algo) {
        algorithmInstance = algo;
    }

    public void doSome() {
        algorithmInstance.execAlgorithm();
    }
}

interface Algorithm {
    void execAlgorithm();
}

class AlgorithmOne implements Algorithm {
    @Override
    public void execAlgorithm() {
        System.out.println("Executing algorithm One");
    }
}

class AlgorithmTwo implements Algorithm {
    @Override
    public void execAlgorithm() {
        System.out.println("Executing algorithm Two");
    }
}

class EntryPoint {
    public static void main(String[] args) {
        CodeThatUsesSomeAlgorithm obj = new CodeThatUsesSomeAlgorithm();
        obj.setAlgorithm(new AlgorithmOne());
        obj.doSome();
        obj.setAlgorithm(new AlgorithmTwo());
        obj.doSome();
    }
}
