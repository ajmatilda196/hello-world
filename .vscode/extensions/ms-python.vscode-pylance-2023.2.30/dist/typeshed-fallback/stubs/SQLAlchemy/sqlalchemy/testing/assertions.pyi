from _typeshed import Incomplete

def expect_warnings(*messages, **kw): ...
def expect_warnings_on(db, *messages, **kw) -> None: ...
def emits_warning(*messages): ...
def expect_deprecated(*messages, **kw): ...
def expect_deprecated_20(*messages, **kw): ...
def emits_warning_on(db, *messages): ...
def uses_deprecated(*messages): ...
def global_cleanup_assertions() -> None: ...
def eq_regex(a, b, msg: Incomplete | None = ...) -> None: ...
def eq_(a, b, msg: Incomplete | None = ...) -> None: ...
def ne_(a, b, msg: Incomplete | None = ...) -> None: ...
def le_(a, b, msg: Incomplete | None = ...) -> None: ...
def is_instance_of(a, b, msg: Incomplete | None = ...) -> None: ...
def is_none(a, msg: Incomplete | None = ...) -> None: ...
def is_not_none(a, msg: Incomplete | None = ...) -> None: ...
def is_true(a, msg: Incomplete | None = ...) -> None: ...
def is_false(a, msg: Incomplete | None = ...) -> None: ...
def is_(a, b, msg: Incomplete | None = ...) -> None: ...
def is_not(a, b, msg: Incomplete | None = ...) -> None: ...

is_not_ = is_not

def in_(a, b, msg: Incomplete | None = ...) -> None: ...
def not_in(a, b, msg: Incomplete | None = ...) -> None: ...

not_in_ = not_in

def startswith_(a, fragment, msg: Incomplete | None = ...) -> None: ...
def eq_ignore_whitespace(a, b, msg: Incomplete | None = ...) -> None: ...
def assert_raises(except_cls, callable_, *args, **kw): ...
def assert_raises_context_ok(except_cls, callable_, *args, **kw): ...
def assert_raises_message(except_cls, msg, callable_, *args, **kwargs): ...
def assert_raises_message_context_ok(except_cls, msg, callable_, *args, **kwargs): ...

class _ErrorContainer:
    error: Incomplete

def expect_raises(except_cls, check_context: bool = ...): ...
def expect_raises_message(except_cls, msg, check_context: bool = ...): ...

class AssertsCompiledSQL:
    test_statement: Incomplete
    supports_execution: Incomplete
    def assert_compile(
        self,
        clause,
        result,
        params: Incomplete | None = ...,
        checkparams: Incomplete | None = ...,
        for_executemany: bool = ...,
        check_literal_execute: Incomplete | None = ...,
        check_post_param: Incomplete | None = ...,
        dialect: Incomplete | None = ...,
        checkpositional: Incomplete | None = ...,
        check_prefetch: Incomplete | None = ...,
        use_default_dialect: bool = ...,
        allow_dialect_select: bool = ...,
        supports_default_values: bool = ...,
        supports_default_metavalue: bool = ...,
        literal_binds: bool = ...,
        render_postcompile: bool = ...,
        schema_translate_map: Incomplete | None = ...,
        render_schema_translate: bool = ...,
        default_schema_name: Incomplete | None = ...,
        from_linting: bool = ...,
        check_param_order: bool = ...,
    ) -> None: ...

class ComparesTables:
    def assert_tables_equal(self, table, reflected_table, strict_types: bool = ...) -> None: ...
    def assert_types_base(self, c1, c2) -> None: ...

class AssertsExecutionResults:
    def assert_result(self, result, class_, *objects) -> None: ...
    def assert_list(self, result, class_, list_) -> None: ...
    def assert_row(self, class_, rowobj, desc) -> None: ...
    def assert_unordered_result(self, result, cls, *expected): ...
    def sql_execution_asserter(self, db: Incomplete | None = ...): ...
    def assert_sql_execution(self, db, callable_, *rules): ...
    def assert_sql(self, db, callable_, rules): ...
    def assert_sql_count(self, db, callable_, count) -> None: ...
    def assert_multiple_sql_count(self, dbs, callable_, counts): ...
    def assert_execution(self, db, *rules) -> None: ...
    def assert_statement_count(self, db, count): ...
