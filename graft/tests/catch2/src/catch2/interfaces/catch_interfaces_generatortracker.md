# tests/catch2/src/catch2/interfaces/catch_interfaces_generatortracker.hpp

- GeneratorUntypedBase · class · L19-L75 — class GeneratorUntypedBase
- next · function · L33-L33 — virtual bool next() = 0;
- stringifyImpl · function · L36-L36 — virtual std::string stringifyImpl() const = 0;
- GeneratorUntypedBase · function · L39-L39 — GeneratorUntypedBase() = default;
- GeneratorUntypedBase · function · L42-L42 — GeneratorUntypedBase(GeneratorUntypedBase const&) = default;
- countedNext · function · L57-L57 — bool countedNext();
- currentElementIndex · function · L59-L59 — std::size_t currentElementIndex() const { return m_currentElementIndex; }
- currentElementAsString · function · L74-L74 — StringRef currentElementAsString() const;
- IGeneratorTracker · class · L80-L86 — class IGeneratorTracker
- hasGenerator · function · L83-L83 — virtual auto hasGenerator() const -> bool = 0;
- getGenerator · function · L84-L84 — virtual auto getGenerator() const -> Generators::GeneratorBasePtr const& = 0;
- setGenerator · function · L85-L85 — virtual void setGenerator( Generators::GeneratorBasePtr&& generator ) = 0;
