// sql.monarch.ts
// Auto-generated Monaco language definition

export const sqlLanguage = {
  "defaultToken": "",
  "tokenPostfix": ".sql",
  "ignoreCase": true,
  "keywords": [
    "ADD",
    "ALL",
    "ALTER",
    "AND",
    "AS",
    "ASC",
    "BETWEEN",
    "BLOB",
    "BOOL",
    "BOOLEAN",
    "BY",
    "CHAR",
    "CHECK",
    "COLUMN",
    "CREATE",
    "CROSS",
    "DATABASE",
    "DATE",
    "DATETIME",
    "DECIMAL",
    "DELETE",
    "DESC",
    "DISTINCT",
    "DOUBLE",
    "DROP",
    "FALSE",
    "FLOAT",
    "FOREIGN",
    "FROM",
    "FULL",
    "GROUP",
    "HAVING",
    "IN",
    "INDEX",
    "INNER",
    "INSERT",
    "INT",
    "INTEGER",
    "INTO",
    "IS",
    "JOIN",
    "KEY",
    "LEFT",
    "LIKE",
    "LIMIT",
    "MODIFY",
    "NOT",
    "NULL",
    "NUMERIC",
    "OFFSET",
    "ON",
    "OR",
    "ORDER",
    "PRIMARY",
    "RIGHT",
    "SELECT",
    "SET",
    "TABLE",
    "TEXT",
    "TIME",
    "TIMESTAMP",
    "TOP",
    "TRUE",
    "UNIQUE",
    "UPDATE",
    "VALUES",
    "VARCHAR",
    "VIEW",
    "WHERE"
  ],
  "operators": [
    "!=",
    "%",
    "(",
    ")",
    "*",
    "+",
    ",",
    "-",
    ".",
    "/",
    "<",
    "<=",
    "<>",
    "=",
    ">",
    ">=",
    "[^"
  ],
  "symbols": ",|>|<|<=|>=|=|<>|\\-|\\(|/|\\+|\\[\\^|%|\\)|\\*|!=|\\.",
  "brackets": [
    {
      "open": "(",
      "close": ")",
      "token": "delimiter.parenthesis"
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
        "/<=/",
        "operator"
      ],
      [
        "/>=/",
        "operator"
      ],
      [
        "/<>/",
        "operator"
      ],
      [
        "/\\[\\^/",
        "operator"
      ],
      [
        "/!=/",
        "operator"
      ],
      [
        "/,/",
        "operator"
      ],
      [
        "/>/",
        "operator"
      ],
      [
        "/</",
        "operator"
      ],
      [
        "/=/",
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
        "///",
        "operator"
      ],
      [
        "/\\+/",
        "operator"
      ],
      [
        "/%/",
        "operator"
      ],
      [
        "/\\)/",
        "operator"
      ],
      [
        "/\\*/",
        "operator"
      ],
      [
        "/\\./",
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

export const sqlLanguageConfig = {
  "brackets": [
    [
      "(",
      ")"
    ]
  ],
  "autoClosingPairs": [
    {
      "open": "(",
      "close": ")"
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
      "open": "'",
      "close": "'"
    }
  ]
};

// Register with Monaco Editor
export function registerSqlLanguage(monaco: any) {
  monaco.languages.register({ id: 'sql' });
  monaco.languages.setMonarchTokensProvider('sql', sqlLanguage);
  monaco.languages.setLanguageConfiguration('sql', sqlLanguageConfig);
}
