// python.monarch.ts
// Auto-generated Monaco language definition

export const pythonLanguage = {
  "defaultToken": "",
  "tokenPostfix": ".python",
  "keywords": [
    "False",
    "None",
    "True",
    "and",
    "as",
    "break",
    "continue",
    "from",
    "import",
    "in",
    "is",
    "not",
    "or",
    "pass",
    "return"
  ],
  "operators": [
    "!=",
    "%",
    "(",
    "([^",
    ")",
    "*",
    "**",
    "+",
    ",",
    "-",
    ".",
    "/",
    "//",
    ":",
    "<",
    "<=",
    "=",
    "==",
    ">",
    ">=",
    "[",
    "\\\\]|\\\\.)*",
    "]",
    "{",
    "|",
    "}"
  ],
  "symbols": "\\{|=|\\*|!=|\\}|,|:|<=|\\-|\\*\\*|\\(|\\+|\\||%|\\\\\\\\\\]\\|\\\\\\\\\\.\\)\\*|\\]|//|\\(\\[\\^|==|\\)|<|\\.|>|>=|/|\\[",
  "brackets": [
    {
      "open": "(",
      "close": ")",
      "token": "delimiter.parenthesis"
    },
    {
      "open": "[",
      "close": "]",
      "token": "delimiter.square"
    },
    {
      "open": "{",
      "close": "}",
      "token": "delimiter.curly"
    }
  ],
  "tokenizer": {
    "root": [
      {
        "include": "@whitespace"
      },
      [
        "/\\d+(\\.\\d+)?([eE][+-]?\\d+)?/",
        "number"
      ],
      [
        "/\"([^\"\\\\]|\\\\.)*\"/",
        "string"
      ],
      [
        "/'([^'\\\\]|\\\\.)*'/",
        "string"
      ],
      [
        "/[a-zA-Z_][\\w]*/",
        {
          "cases": {
            "@keywords": "keyword",
            "@default": "identifier"
          }
        }
      ],
      [
        "/\\\\\\\\\\]\\|\\\\\\\\\\.\\)\\*/",
        "operator"
      ],
      [
        "/\\(\\[\\^/",
        "operator"
      ],
      [
        "/!=/",
        "operator"
      ],
      [
        "/<=/",
        "operator"
      ],
      [
        "/\\*\\*/",
        "operator"
      ],
      [
        "////",
        "operator"
      ],
      [
        "/==/",
        "operator"
      ],
      [
        "/>=/",
        "operator"
      ],
      [
        "/\\{/",
        "operator"
      ],
      [
        "/=/",
        "operator"
      ],
      [
        "/\\*/",
        "operator"
      ],
      [
        "/\\}/",
        "operator"
      ],
      [
        "/,/",
        "operator"
      ],
      [
        "/:/",
        "operator"
      ],
      [
        "/\\-/",
        "operator"
      ],
      [
        "/\\(/",
        "operator"
      ],
      [
        "/\\+/",
        "operator"
      ],
      [
        "/\\|/",
        "operator"
      ],
      [
        "/%/",
        "operator"
      ],
      [
        "/\\]/",
        "operator"
      ],
      [
        "/\\)/",
        "operator"
      ],
      [
        "/</",
        "operator"
      ],
      [
        "/\\./",
        "operator"
      ],
      [
        "/>/",
        "operator"
      ],
      [
        "///",
        "operator"
      ],
      [
        "/\\[/",
        "operator"
      ],
      [
        "/[()[\\]{}]/",
        "@brackets"
      ],
      [
        "/[;,.]/",
        "delimiter"
      ]
    ],
    "whitespace": [
      [
        "/[ \\t\\r\\n]+/",
        ""
      ],
      [
        "/--.*$/",
        "comment"
      ],
      [
        "/\\/\\/.*$/",
        "comment"
      ],
      [
        "/\\/\\*/",
        "comment",
        "@comment"
      ]
    ],
    "comment": [
      [
        "/[^/*]+/",
        "comment"
      ],
      [
        "/\\*\\//",
        "comment",
        "@pop"
      ],
      [
        "/[/*]/",
        "comment"
      ]
    ]
  }
};

export const pythonLanguageConfig = {
  "brackets": [
    [
      "(",
      ")"
    ],
    [
      "[",
      "]"
    ],
    [
      "{",
      "}"
    ]
  ],
  "autoClosingPairs": [
    {
      "open": "(",
      "close": ")"
    },
    {
      "open": "[",
      "close": "]"
    },
    {
      "open": "{",
      "close": "}"
    },
    {
      "open": "'",
      "close": "'"
    }
  ],
  "surroundingPairs": [
    {
      "open": "(",
      "close": ")"
    },
    {
      "open": "[",
      "close": "]"
    },
    {
      "open": "{",
      "close": "}"
    },
    {
      "open": "'",
      "close": "'"
    }
  ]
};

// Register with Monaco Editor
export function registerPythonLanguage(monaco: any) {
  monaco.languages.register({ id: 'python' });
  monaco.languages.setMonarchTokensProvider('python', pythonLanguage);
  monaco.languages.setLanguageConfiguration('python', pythonLanguageConfig);
}
