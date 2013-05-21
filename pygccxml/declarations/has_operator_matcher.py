from . import type_traits
from . import class_declaration
from . import matchers
from . import cpptypes


def has_public_binary_operator(type_, operator_symbol):
    """returns True, if `type_` has public binary operator, otherwise False"""
    def decay(type_):
        type_ = type_traits.remove_reference( type_ )
        type_ = type_traits.remove_pointer( type_ )
        type_ = type_traits.remove_alias( type_ )
        type_ = type_traits.remove_cv( type_ )
        type_ = type_traits.remove_declarated( type_ )
        return type_
    type_ = decay(type_)
    assert isinstance(type_, class_declaration.class_t)

    if type_traits.is_std_string(type_) or type_traits.is_std_wstring(type_):
        # In some case compare operators of std::basic_string are not
        # instantiated
        return True

    # search free functions
    declarated = cpptypes.declarated_t(type_)
    const = cpptypes.const_t(declarated)
    reference = cpptypes.reference_t(const)
    operators = type_.top_parent.operators(
        function=lambda decl: not decl.is_artificial,
        arg_types=[reference, None],
        symbol=operator_symbol,
        allow_empty=True,
        recursive=True)
    if operators:
        return True
    all_bases = [type_] + [ x.related_class for x in type_.recursive_bases
                  if x.access_type == class_declaration.ACCESS_TYPES.PUBLIC
                ]

    for cls in all_bases:
        operators = cls.member_operators(
            function=matchers.custom_matcher_t(
                lambda decl: not decl.is_artificial) &
            matchers.access_type_matcher_t('public'),
            symbol=operator_symbol, allow_empty=True, recursive=False)

        if not operators:
            continue

        for op in operators:
            arg = decay(op.argument_types[0])
            if arg in all_bases:
                return True
        return False  # do not match further base types (name hiding)
    return False


def has_public_equal(decl_type):
    """returns True, if class has public operator==, otherwise False"""
    return has_public_binary_operator(decl_type, '==')


def has_public_less(decl_type):
    """returns True, if class has public operator<, otherwise False"""
    return has_public_binary_operator(decl_type, '<')
