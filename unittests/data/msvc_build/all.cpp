#include "abstract_classes.hpp"
#include "attributes.hpp"
#include "bit_fields.hpp"
#include "complex_types.hpp"
#include "core_cache.hpp"
#include "core_class_hierarchy.hpp"
#include "core_diamand_hierarchy_base.hpp"
#include "core_diamand_hierarchy_derived1.hpp"
#include "core_diamand_hierarchy_derived2.hpp"
#include "core_diamand_hierarchy_final_derived.hpp"
#include "core_membership.hpp"
#include "core_ns_join_1.hpp"
#include "core_ns_join_2.hpp"
#include "core_ns_join_3.hpp"
#include "core_overloads_1.hpp"
#include "core_overloads_2.hpp"
#include "core_types.hpp"
#include "declarations_calldef.hpp"
#include "declarations_comparison.hpp"
#include "declarations_enums.hpp"
#include "declarations_for_filtering.hpp"
#include "declarations_variables.hpp"
#include "demangled.hpp"
#include "free_operators.hpp"
#include "has_public_binary_operator_traits.hpp"
#include "include_all.hpp"
#include "include_std.hpp"
#include "indexing_suites2.hpp"
#include "noncopyable.hpp"
#include "patcher.hpp"
#include "remove_template_defaults.hpp"
#include "string_traits.hpp"
#include "type_as_exception_bug.h"
#include "type_traits.hpp"
#include "typedefs1.hpp"
#include "typedefs2.hpp"
#include "typedefs_base.hpp"
#include "unnamed_classes.hpp"
#include "unnamed_enums_bug1.hpp"
#include "unnamed_enums_bug2.hpp"
#include "unnamed_ns_bug.hpp"
#include "vector_traits.hpp"

namespace declarations{ namespace variables{

int static_var = 0;
}}

void use_decls(){	
	declarations::enums::ENumbers enumbers;
	declarations::enums::data::EColor ecolor;
}